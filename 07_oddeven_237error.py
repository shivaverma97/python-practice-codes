list1 = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
i=0
while i >=0 :
    if list1[i]%2==0 :
        print(list1[i])
        i=i+1
    elif list1[i]==237:
        print("237 encountered, stopping program... ")
        break
    elif list1[i]%2!=0 :
        print("",end="")
        i=i+1


