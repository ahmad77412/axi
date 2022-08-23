import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dump import p_dump
    p_dump()
elif bit == '32bit':
    from dump import p_dump
    p_dump()