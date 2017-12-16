import random
master=open("gigorso.txt","r")
opt=input("ammount?")
print("reading")
m=master.read()
for i in range(0,int(opt)):
	print("o")
	f=open(str(random.randint(0,999999))+".txt","w")
	print("w")
	f.write(m)
	print("c")
	f.close()
quit()
	
