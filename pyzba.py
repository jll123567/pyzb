# import
import random

# runtime
master = open("master.txt", "r")
r = master.read()
for i in range(100):
    f = open(str(random.randint(0, 9999))+".txt", "w")
    f.write(r)
    f.close()
master.close()
