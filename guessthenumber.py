import random
rand_num = random.randint(1,10)
print(''' WELCOME TO THE GAME OF GUESS :) 
 LETS TRY YOUR LUCK TODAY''')


Guess=[]

i=0
while (i>=0) :
    g=int(input("Your Guess please : "))
    Guess.append(g)

    if (g == rand_num) :
        print(" WOW!! Nice Guess ")
        print(f'The number of tries were :{len(Guess)}')
        break
    elif (g>rand_num):
        print("")
        i=i+1
        
    else :
        print(" OOPS!! try again with larger number ")
        i=i+1


