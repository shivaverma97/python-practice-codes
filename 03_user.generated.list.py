i=0
list1=[]
tuple1=()
while i>=0 :
    data = input("Enter Data :")
    list1.append(data)
    tuple1=tuple(list1)
    i+=1
    if data == "end" :
        list1.remove("end")
        tuple1=tuple(list1)
        break


print(list1)
print(tuple1)

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)



