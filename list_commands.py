import os
num_of_inp = int(input())
list_1 = []

for i in range(num_of_inp):
    command = str(input())
    if command[0:6] == 'insert' :
        inp, index, value = command.split(" ")
        index = int(index)
        value = int(value)
        list_1.insert(index, value)

    if command[0:5] == 'print' :
        print(list_1)
    
    if command[0:6] == 'remove' :
        inp, value = command.split(" ")
        value = int(value)
        list_1.remove(value)
    
    if command[0:6] == 'append' :
        inp, value = command.split(" ")
        value = int(value)
        list_1.append(value)
     
    if command[0:4] == 'sort' :
        list_1.sort()
    
    if command[0:3] == 'pop' :
        list_1.pop(-1)
    
    if command[0:7] == 'reverse' :
        list_1.reverse()
    
