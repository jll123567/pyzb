import random
word=""
empty=open("gigorso.txt","w")
empty.close()
for i in range(0,1500):
	print("f")
	word=word+str(random.randint(0,1))
print(word)
#name="gigorso"
print("writeing")
file=open("gigorso.txt","w")
file.write((word*100000))
file.close()
print("done")
quit()