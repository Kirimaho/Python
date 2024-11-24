import subprocess as sub
import time
import sys 

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
		print("Monitor mode has been set succesfuly")
	if "wlan0" not in out:
		print("Wifi adapter not found")
	if "Monitor" not in out:
		clear()
		print("There has been an error setting up monitor mode, check config")

def program_clear():
	sub.check_output("sudo airmon-ng stop wlp4s0mon", shell=True)
	clear()
	print("Managed mode have been set succesfuly")

def close():
	sys.exit()


def main():
	user = get_user()
	dec = input(f"Hello {user} (E)xecute  (C)lear   E(X)it: ").lower()

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
		print("Invalid option. Please try again")

if __name__ == "__main__":
    main()
