 #!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo ="""\033[1;97m
\033[1;94m           ###    ##     ## #### 
\033[1;92m          ## ##    ##   ##   ##  
\033[1;94m         ##   ##    ## ##    ##  
\033[1;92m        ##     ##    ###     ##  
\033[1;93m        #########   ## ##    ##  
\033[1;94m        ##     ##  ##   ##   ##  
\033[1;92m        ##     ## ##     ## #### 
--------------------------------------------------
 Owner    : MALIK AHMAD AWAN
 TEAM     : RIAZ X AHMAD
 TOOL     : MAIN MENU
 Version  : 5.3
--------------------------------------------------
Turn on & off flight (airplane) mode before use
--------------------------------------------------
PAID TOOL UPDATE AFTER 2 DAYS
--------------------------------------------------"""

def ahmad():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print('   1 FILE CLONING PAID ')
    print('   2 DUMPING TOOL PAID ')
    print('   3 RANDOM UID PAK PAID ')
    print('   4 OLD UID PAID ')
    print('   E_____EXIT')
    print('')
    _ahmad___ = input('       Choose option : ')
    if _ahmad___ in ('1', '01'):
        os.system('python file.py')
    if _ahmad___ in ('2', '02'):     
        os.system('python dump.py')
    if _ahmad___ in ('3', '03'):     
        os.system('python uid.py')
    if _ahmad___ in ('4', '04'):     
        os.system('python old.py')
    if _ahmad___ in ('5', '05'):     
        os.system('python old.py')
    if _ahmad___ in ('E', 'ee'):
        pass

print('chk update')
os.system('git pull')
ahmad()
