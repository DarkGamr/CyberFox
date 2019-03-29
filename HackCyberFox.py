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
os.system("cd ../home/CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt")
update = filecmp.cmp('../home/CyberFox/ver.txt', '../home/CyberFox/update_check/ver.txt')
os.system("cd ../home && cd CyberFox")
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
	os.system("cp update.py ../home")
	
	os.system("cd ../home && python3 update.py")
	
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
print(colored("=version 1.2", 'blue'))
print("")
print("")
print("")
print("")
print("")
print("")
      


text = input(colored('cbf> ', 'red'))
G ="show optinals"
W ="help"
M ="use modules qiwi/hacker"

if text == M:
	os.system("cd ../home/CyberFox/modules && python3 qiwimodules.py")
if text == W:
	
	action = input(colored("Хотите связаться с разработчиком? Да/Нет ", 'green'))
	if action == "Да" or "да": 
		os.system("termux-open https://vk.com/shift_tv3")
	elif action == "Нет" or "нет" :
		print(colored("use command: show optinals", 'blue'))

if text == G:
	print("")
	print("")
	print("")
	
	print(colored("=  modules:",  'green'))
	print(colored("|", 'blue'))
	print("=  use modules qiwi/hacker ")
    
