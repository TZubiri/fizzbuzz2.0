
DATA = ["1", "2" ,"3" ,"4","5", "6", "7", "8", "123","", "105","180","blabla", "bla180"]



def divisibleby5(s):
	if s[-1] == "0" or s[-1] == "5":
		return True
	else:
		return False

def mod3char(x):
	if x == "0" or x=="3" or x=="6" or x=="9":
		return "0"
	if x == "1" or x=="4" or x=="7":
		return "1"
	if x == "2" or x=="5" or x=="8":
		return "2"
	
def add3 (x,y):
	x = mod3char(x)
	y = mod3char(y)
	if x == "0" and y == "0":
		return "0"
	if x == "0" and y == "1":
		return "1"
	if x == "0" and y == "2":
		return "2"
	if x == "1" and y == "0":
		return "1"
	if x == "1" and y == "1":
		return "2"
	if x == "1" and y == "2":
		return "0"
	if x == "2" and y == "0":
		return "2"
	if x == "2" and y == "1":
		return "0"
	if x == "2" and y == "2":
		return "1"
	
	
def mod3string(string):
	accum = "0"
	for c in string:
		accum = add3(c,accum)
	return accum

def validate(x):
	if 0<len(x)<=4:
		return True
	else:
		return False
	for char in x:
		if x not in "0123456789":
			return False
	

for x in DATA:
	try:

		if validate(x):
			pass
		else:
			print("")
			continue

		div3 = mod3string(x) == '0'	
		div5 = divisibleby5(x)
		if div3:
			print("Fizz",end="")
		if div5:
			print("Buzz",end="")
		if not div3 and not div5:
			print(x,end="")
		print("") #newline
	except Exception as e:
		print(e)
