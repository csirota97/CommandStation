for i in range(16):
	f = open("prog{0}.py".format(i), "w+")
	f.write("def set():\n\tprint('prog{0}')".format(i))
	print("from Prog_Files import prog{0} as prog{0}".format(i))

print("")


for i in range(16):
	print("elif data == 'PROG{0}':\nprog{0}.set()".format(i))
