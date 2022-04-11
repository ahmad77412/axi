#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('axi_enc.py'):
    os.system('curl -L https://raw.githubusercontent.com/ahmad77412/axi/axi_enc.py')
    os.system('clear')
if not os.path.isfile('axi_enc.py'):
    os.system('curl -L https://raw.githubusercontent.com/ahmad77412/axi/axi_enc.py')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/ahmad77412/axi/axi_enc.py')
if 'axii.py' in go:
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
else:
    os.system('rm -rf axi')
    os.system('curl -L https://raw.githubusercontent.com/ahmad77412/axi/axi_enc.py')
    os.system('curl -L https://raw.githubusercontent.com/ahmad77412/axi/axi_enc.py')
    if bit == '64bit':
        from Jutt import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
