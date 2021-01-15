str1 = str(input("enter here..."))
i = 0
while i < len(str1) :
    if  str1[i]== str1[i].lower() :
        print(f"yes lower case {str1[i]} is present")
        i=i+1
    else:
        i=i+1