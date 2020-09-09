import sys

def encrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in key:
        for i in range(len(msg)):
            if i == 0:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[-1])
            else:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[i-1])

            while tmp > 255:
                tmp -= 256
            msg[i] = chr(tmp)
    return ''.join(msg)

def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)

def bruteforce():
    cipherfile = open('ciphertext', 'rb')
    ciphertext = cipherfile.read()
    wordlist = open('/usr/share/wordlists/rockyou.txt', 'r')
    out = open("dec.txt", 'w+')
    for w in wordlist:
        # print('testing ->' + w.strip())
        dec = decrypt(w.strip(), ciphertext)
        if 'the ' in dec or 'be ' in dec or 'and ' in dec or 'of ' in dec:
            print(dec)
        try:
            decoded = dec.decode('utf-8')
            print('found possible key-> {0}'.format(w.strip()))
            out.write(decoded)
        except:
            continue
    out.close()


if __name__ == '__main__':
    #if sys.argv[1] == None:
    bruteforce()
    # else:
    #     cipherfile = open('ciphertext', 'rb')
    #     ciphertext = cipherfile.read()
    #     print decrypt(sys.argv[1], ciphertext)
