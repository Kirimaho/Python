import subprocess
import time

def idle(sec):
	time.sleep(sec)

user = subprocess.check_output(["whoami"], text=True)
dec = input(f"Hello {user} (E)xecute or (C)lear: ").lower()

while dec not in ("c", "e"):
	dec = input("Please, press C to clear or E to execute:  ").lower()



if dec == "e": 
	subprocess.run("sudo ip link set wlxa0d768107152 name wlan0", shell=True)
	subprocess.run("iwconfig")
	subprocess.run(["sudo", "airmon-ng", "start", "wlan0"])
	subprocess.run(["sudo", "airmon-ng", "start", "wlp4s0"])
	subprocess.run(["clear"])
	output = subprocess.check_output(["iwconfig"], text=True)
	if "Monitor" in output:
		subprocess.run(["clear"])
		print("Monitor mode has been set succesfuly")
	if "wlan0" not in output:
		print("Wifi adapter not found")
	if "Monitor" not in output:
		subprocess.run(["clear"])
		print("There has been an error setting up monitor mode, check config")


if dec == "c":
	subprocess.run(["clear"])
	subprocess.run("sudo airmon-ng stop wlp4s0mon", shell=True)
	outpute = subprocess.check_output(["iwconfig"], text=True)
	if "Managed" in outpute:
		subprocess.run(["clear"])
		print("Managed mode has been set succesfuly")

