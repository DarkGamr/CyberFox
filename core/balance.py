from core.colors import *
from SimpleQIWI import *
import time

def bal():
	try:
		tok = input(B+"\n[cbf]"+W+" Enter token: ")
		pho = input(B+"[cbf]"+W+" Enter phone: ")
		api = QApi(token=tok, phone=pho)
		if api.balance != 0:
			print(G+"[#]"+W+" Balance Detect")
			print(G+"[#]"+W+" Balance =", api.balance)
			time.sleep(7)
	except:
		print(R+"[err]"+W+" Balance not found")
		time.sleep(7)
		pass