number_list = []

num = int(input("enter number \n"))
number_list.append(num)
i=0
while i >= 0 :
    
    cont = input("want to continue ? \n")
    if cont=='y':
        num = int(input("enter number \n" ))
        number_list.append(num)
        i=i+1
    elif cont=='n':
        break

print(number_list)

k = 1
temp_min = number_list[0]
while k < len(number_list) :
    if temp_min < number_list[k] :
        k=k+1
    elif temp_min > number_list[k] :
        temp_min = number_list[k]
        k=k+1

j = 1
temp_max = number_list[0]
while j < len(number_list) :
    if temp_max > number_list[j] :
        j=j+1
    elif temp_max < number_list[j] :
        temp_max = number_list[j]
        j=j+1

print(f'max input value : {temp_max}')
print(f'min input value : {temp_min}')


    