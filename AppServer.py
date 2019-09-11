import socket
from Prog_Files import prog0 as prog0
from Prog_Files import prog1 as prog1
from Prog_Files import prog2 as prog2
from Prog_Files import prog3 as prog3
from Prog_Files import prog4 as prog4
from Prog_Files import prog5 as prog5
from Prog_Files import prog6 as prog6
from Prog_Files import prog7 as prog7
from Prog_Files import prog8 as prog8
from Prog_Files import prog9 as prog9
from Prog_Files import prog10 as prog10
from Prog_Files import prog11 as prog11
from Prog_Files import prog12 as prog12
from Prog_Files import prog13 as prog13
from Prog_Files import prog14 as prog14
from Prog_Files import prog15 as prog15


def main():
	host = socket.getfqdn()
	print(host)
	port = 19891

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', port))

	print("Server Started")

	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')

		print("Message from: " + str(addr))
		print("From user: " + data)

		if data == 'PROG0':
			prog0.set()
		elif data == 'PROG1':
			prog1.set()
		elif data == 'PROG2':
			prog2.set()
		elif data == 'PROG3':
			prog3.set()
		elif data == 'PROG4':
			prog4.set()
		elif data == 'PROG5':
			prog5.set()
		elif data == 'PROG6':
			prog6.set()
		elif data == 'PROG7':
			prog7.set()
		elif data == 'PROG8':
			prog8.set()
		elif data == 'PROG9':
			prog9.set()
		elif data == 'PROG10':
			prog10.set()
		elif data == 'PROG11':
			prog11.set()
		elif data == 'PROG12':
			prog12.set()
		elif data == 'PROG13':
			prog13.set()
		elif data == 'PROG14':
			prog14.set()
		elif data == 'PROG15':
			prog15.set()
	c.close()


if __name__ == '__main__':
	main()





