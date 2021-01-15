a = str(input("enter str : "))
n = int(input("no. of copies :"))

# sub = a[0] + a[1]
# print(sub)

for i in range(1, n+1):
    sub = a[0] + a[1]
    print(sub,end="")
    sub = sub + sub


