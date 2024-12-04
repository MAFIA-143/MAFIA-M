
import os, platform

 

try:

 

        import requests

 

except:

 

        os.system('pip2 install requests')

 

 

 

bit = platform.architecture()[0]

 

if bit == "64bit":

        os.system('xdg-open https://www.youtube.com/@mafiams16')

 

        from file9 import MX1

 

        MAFIA_Main()

 

 

 

elif bit == "32bit":

 

        os.system('xdg-open https://www.youtube.com/@mafiams16')

 

        os.system('python file9.py')
