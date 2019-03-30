import os
from core.colors import *
from SimpleQIWI import *
from core import balance
from core import main
from core import vivod
from time import sleep as ts
from core.banner import *

os.system("clear")
#modules
def main():
	os.system("clear")
	ts(5)
	print(banner)
	try:
		van = input(R+"cbf>> "+W)
		if van == "use modules qiwi/hacker":
			ts(3)
			print("")
			print("")
			mod = input(R+"cbf[hack/checker?]: "+W)
			if mod == "checker":
				balance.bal()
				main()
			elif mod == "hack":
				vivod.viv()
				main()
			
		elif van == "help":
			from core import help
			main()
			
		elif van == "quit":
			print(R+"good bye!"+W)

		else:
			print(R+"[X]"+W+" Wrong command -> " + van)
			ts(2)
			main()

	except(KeyboardInterrupt):
		print(R+"[X]"+W+" Exiting...")
if __name__ == '__main__':
	main()