import psutil
import re


def ext(cad):
    return re.findall(r"'(.*?)'", cad)

def interfaces():
	addrs = psutil.net_if_addrs()
	i = addrs.keys()

	for icn in i:
		ext(icn)
		print(icn) #print is temporal, here is the information i want to get outside this function
		
if __name__ == "__main__":
	interfaces()
