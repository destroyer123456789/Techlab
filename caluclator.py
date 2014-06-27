a = raw_input('Do you want to use the calculator?')
if a.lower() == "yes":
	print 'If you want to get decimal answers make your first number a decimal(8.0,33.3,6.00,etc.)'
	x = int(raw_input('Type a number:'))
	y = int(raw_input('Type another number:'))
	z = raw_input('Type in an operation.(+,-,*,/)')
	total = 0
	if z == "+":
		total = x + y
		print total
	elif z == '-':
		total = x - y
		print total
	elif z == '*':
		total = x * y
		print total
	elif z == '/':
		total = x/y
		print total
c = raw_input('Do you want to do special operations?')
if c.lower() == 'yes':
	d = int(raw_input('Type a number'))
	e = raw_input('Choose an operation(Options: square,cube,fourth)')
	if e == 'square':
		total = d*d
		print total
	elif e == 'cube':
		total = d*d*d
		print total
	elif e == 'fourth':
		total = d*d*d*d
		print total
b = raw_input('Do you want to continue using the calculator?') 
if b.lower() == "yes":
	x = int(raw_input('Type a number:'))
	y = int(raw_input('Type another number:'))
	z = raw_input('Type in an operation.(+,-,*,/)')
	total = 0
	if z == "+":
		total = x + y
		print total
	elif z == '-':
		total = x - y
		print total
	elif z == '*':
		total = x * y
		print total
	elif z == '/':
		total = x/y
		print total
print "Thanks for using my calculator."

x = int(raw_input('Type a number: '))
total = 0
for y in range(1,x+1):
	if y % 2 == 0:
		total = total + y
print total