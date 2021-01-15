num_list = []
odd_list = []  
k=0
while k>=0 :
    num= int(input("enter num :"))
    if num == 0 :
        break
    else:
        num_list.append(num)
j=0
while j<(len(num_list)-1):
    i=0
    while i<len(num_list) :
        pro = (num_list[j]*num_list[i])
        if pro%2 == 0 :
            i=i+1
        elif pro%2 != 0 :
            odd_list.append(pro)
            i=i+1
    j=j+1

print(odd_list) 
        
