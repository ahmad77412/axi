import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from axi import mengecek_
    mengecek_()
elif bit == '32bit':
    from axi import mengeck_
    mengeck_()
