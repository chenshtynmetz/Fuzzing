from scapy.all import *


# check the packet
def show(pkt):
	sum = 1
	try:
		data = pkt["Raw"].load
		try:
			data2 = data.decode()
		except UnicodeDecodeError:
			if len(data) > 255:
				print("fuzzing detected")
				exit(0)
			return
		if data2[0] == 'S' and data2[1] == 'S' and data2[2] == 'H':
			# check if the data is to long
			if len(data2) > 255:
				print("fuzzing detected")
				exit(0)
			#check if the end of the string is legall
			if data2[len(data2) -1] !='\n' or data2[len(data2) -2 ] != '\r':
				print("fuzzing detected")
				exit(0)
		#check if the data is seq ot the same char
		for i in range(1, len(data2)):
			if sum > 3:
				print("fuzzing detected")
				exit(0)
			elif data2[i-1] == data2[i]:
				sum = sum + 1
			else:
				sum = 1
	except IndexError:
		return 
	

if __name__ == '__main__':
	interface = input("Please enter the name of your interface:\n")
	pkt = sniff(iface= interface, filter = "port 22", prn=show)