import random
import time
master=open("master.txt","w")
m=""
for i in range(0,10000):
    m=m+str(random.randint(0,1))
master.write(m*10000)
master.close()