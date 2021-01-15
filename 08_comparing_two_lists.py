list1=["White", "Black", "Red"]
list2=["Red", "Green"]

print(len(list1))

i=0
while i>=0 :
        if list1[i] in list2 :
            print("",end="")
            if i < (len(list1)-1) :
                 i=i+1
            else :
                break

        else :
            print(list1[i])
            if i < (len(list1)-1) :
                 i=i+1
            else :
                break
        


