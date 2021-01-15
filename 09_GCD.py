num1 = int(input("enter num 1 : "))
num2 = int(input("enter num 2 : "))

list1=[]

if num1 < num2 :
    n = num1
else :
    n = num2

for i in range (1,n+1) :
    if (num1%i == 0) and (num2%i == 0) :
        list1.append(i)

print(f'GCD of {num1} and {num2} is {list1[-1]}')       

        
    