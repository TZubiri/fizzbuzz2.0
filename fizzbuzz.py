
DATA = ["1", "2" ,"3" ,"4","5", "6", "7", "8", "123","", "105","180","blabla", "bla180"]


for x in DATA:
	#debug
	#print(x+"=",end="")
	try:
		try:
			n = int(x)
		except:
			print("")
			continue

		if n%3==0:
			print("Fizz",end="")
		if n%5==0:
			print("Buzz",end="")
		if not n%3==0 and not n%5==0:
			print(x,end="")
		print("") #newline
	except Exception as e:
		print("error")
