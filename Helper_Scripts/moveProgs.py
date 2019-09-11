s = "mv "

for i in range(16):
	s = s + ('prog{0}.py '.format(i))

s = s + ('Prog_Files')

print(s)
