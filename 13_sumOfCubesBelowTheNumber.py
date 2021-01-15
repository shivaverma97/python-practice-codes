cube_list = []
num = int(input("enter number:"))
i=num
while i>0 :
    cube = (i-1)**3
    cube_list.append(cube)
    i=i-1
print(sum(cube_list))
