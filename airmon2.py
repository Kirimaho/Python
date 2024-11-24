import subprocess as sub
import time
import sys 
import argparse
from colorama import init, Fore

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

def main():
	user = get_user()
	print(Fore.MAGENTA + f"Hello {user}" + Fore.RESET)
	parser = argparse.ArgumentParser(description="Argumento")
	parser.add_argument('-e', action='store_true', help="Poner en modo monitor")
	parser.add_argument('-c', action='store_true', help="Quitar de modo monitor")
	arg = parser.parse_args()

	if arg.e: 
		execute()
		check_execute()
		close()

	elif arg.c:
		clear()
		program_clear()
		close()

	else:
		print(Fore.RED + "Invalid option. Please try again" + Fore.RESET)

if __name__ == "__main__":
    main()


