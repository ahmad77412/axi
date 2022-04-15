import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from axi import main_apv
    main_apv()
elif bit == '32bit':
    from axi import main_apv
    main_apv()