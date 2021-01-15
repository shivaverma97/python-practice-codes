import os

n = int(input())
inp = str(input())

inp_list = inp.split()
list_converted = []

for i in range(len(inp_list)) :
    inp_list[i] = int(inp_list[i])
    list_converted.append(inp_list[i])

tup = tuple(list_converted)
hashed = hash(tup)
print(hashed)