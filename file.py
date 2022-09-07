import os
import time
os.system('git pull')

print("")
print("\033[1;32m     Welcome To My Ok Tool");time.sleep(2.0)

import os, platform, time

os.system('git pull')

b = platform.architecture()[0]

if b == '64bit':

    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")

    print("")
    
    print("\033[1;32m     Welcome To My Ok Tool");time.sleep(2.0)
    
    from file64 import Subscraption
    
    Subscraption() 

elif b == '32bit':
	
    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")

    print("")
    
    print("\033[1;32m     Welcome To My Ok Tool");time.sleep(2.0)

    from file import Subscraption
    
    Subscraption() 
