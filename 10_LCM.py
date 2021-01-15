num1 = int(input("enter num 1 : "))
num2 = int(input("enter num 2 : "))



if num1 < num2 :
    n = num2
else :
    n = num1


i=1
while(True) :
    if (i%num1 == 0) and (i%num2 == 0) :
        lcm = i
        break
    else:
        i=i+1
        

print(f'LCM of {num1} and {num2} is {lcm}')       

        