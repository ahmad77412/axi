import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from pak1 import file
    main()
elif bit == '32bit':
    from pak1 import file
    main()