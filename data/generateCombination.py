import random # necessário para utilizar o módulo random


name = input("Enter file name")
file = open("../client/{}.txt".format(name), "w")

n = int(input("N requests"))

write = float(input("Number of writes 0 - 10")) / 10

for i in range(n):
    k = random.random()
    if k < write:
        file.write('w')
    else:
        file.write('r')

file.close()