import os

if __name__ == "__main__":

   try:

       os.system("git pull")

       __import__("axi").menu_apikey()

   except Exception as e: 

       exit(str(e))
