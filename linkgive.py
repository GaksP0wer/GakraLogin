import os
import time
import sys
def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.006)
    

logo = '''

\033[0;31m_____ _              
| __ \ | |             
| | \/ __ _| | ___ __ __ _
| | __ / _` | |/ / '__/ _` |
| |_\ \ (_| | <| | | (_| |
 \____/\__,_|_|\_\_| \__,_|
                            
                            
 _ _        
| | (_)       
| | ___ __ _ _ _ __   
| | / _ \ / _` | | '_ \  
| |___| (_) | (_| | | | | |
\_____/\____/ \__, |_|_| |_|
              __/ |         
             |___/          

'''

animated(logo)

şifre = "Gakra120323"


givenŞifre = input("\033[0;32mŞifreyi Gir Yaramın Topu: ")
if givenŞifre == şifre:
 print("Şifre Onaylandı")
 
 logo2 = '''
 
  _____ _                      
 | __ \ | |                     
 | |__) |_ _ _ __ ___| |                     
 | ___/ _` | '_ \ / _ \ |                     
 | | | (_| | | | | __/ |                     
 |_| \__,_|_| |_|\___|_|                     
     /\ | |                                  
    / \ | |_ __ ___ __ _ _ _ __ _       
   / /\ \ | | '_ ` _ \ / _` | | | |/ _` |      
  / ____ \| | | | | | | (_| | |_| | (_| |      
 /_/ \_\_|_| |_| |_|\__,_|\__, |\__,_|      
                              __/ |            
  _ _ _____ |___/ _ _       
 | | | | / ____| | | | (_)      
 | |__| | ___ ___| | __ ___| | __| |_ _ __  
 | __ |/ _ \/ __| | |_ |/ _ \ |/ _` | | '_ \
 | | | | (_) \__ \ |__| | __/ | (_| | | | | |
 |_| |_|\___/|___/\_____|\___|_|\__,_|_|_| |_|
                                               
 '''
 
 animated(logo2)
 
 Anan = '''
         \033[0;34mLink:https://tavsancik.online
 '''
 
 Anan2 = '''
               \033[0;35mVPN Açarak Gir
 '''
 
 animated(Anan)
 animated(Anan2)
 
else:
  print("\033[1;33mHadi Köyüne Yarrrr")
  