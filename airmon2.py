import subprocess as sub
import time
import sys 
from colorama import init, Fore

#Definiendo modulos

def outp():
	return sub.check_output(["iwconfig"], text=True)

def get_user():
	return sub.check_output(["whoami"], text=True).strip()

def clear():
	sub.run(["clear"])

def execute():
	sub.run("sudo ip link set wlxa0d768107152 name wlan0", shell=True)
	sub.run(["sudo", "airmon-ng", "start", "wlan0"])
	sub.run(["sudo", "airmon-ng", "start", "wlp4s0"])

def check_execute():
	out = outp()

	if "Monitor" in out:
		clear()
		print(Fore.CYAN + "Monitor mode has been set succesfuly" + Fore.RESET)
	if "wlan0" not in out:
		print(Fore.RED + "Wifi adapter not found" + Fore.RESET)
	if "Monitor" not in out:
		clear()
		print("There has been an error setting up monitor mode, check config")

def program_clear():
	try:
		sub.check_output("sudo airmon-ng stop wlp4s0mon", shell=True)
	except:
		print(Fore.RED + "You are not in monitor mode" + Fore.RESET)
		close()
	clear()
	print(Fore.CYAN + "Managed mode have been set succesfuly" + Fore.RESET)

def close():
	sys.exit()

#Cuerpo de el programa

def main():
	user = get_user()
	dec = input(Fore.GREEN + f"Hello {user} | (E)xecute  (C)lear   E(X)it: " + Fore.RESET).lower()

	if dec in "e": 
		execute()
		check_execute()
		close()

	elif dec in "c":
		clear()
		program_clear()
		close()

	elif dec in "x":
		close()

	else:
		print(Fore.RED + "Invalid option. Please try again" + Fore.RESET)

if __name__ == "__main__":
    main()

