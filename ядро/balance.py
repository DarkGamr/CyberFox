from core.colors import *
from SimpleQIWI import *

def bal():
	try:
		tok = input(B+"\n[cbf]"+W+" Enter token: ")
		pho = input(B+"[cbf]"+W+" Enter phone: ")
		api = QApi(token=tok, phone=pho)
		if api.balance != 0:
			print(G+"[#]"+W+" Balance Detect")
			print(G+"[#]"+W+" Balance =", api.balance)
	except:
		print(R+"[err]"+W+" Balance not found")
		pass