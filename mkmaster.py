# runtime
master = open("master.txt", "w")
m = ""
for i in range(0, 10000):
    m += str(0)
master.write(m * 10000)
master.close()
