import random
random_num=random.randint(1,3)



if random_num==1 :
    comp_input="ROCK"
elif random_num==2:
    comp_input="PAPERS"
else :
    comp_input="SCISSORS"

    


# print(random_num)
print('''Wait computer is chosing weapon
        .
        .
        .
        .
        .
        .
        .
        .''')
print("Computer Has chosen his weapon, Your turn now \n")
print("                                              ")
you = input('''Chose your weapon :
               (o) ROCK
               (o) PAPER
               (o) SCISSORS \n''')

def game(x,y):

    if random_num==1:
        if you=="ROCK":
            return None
        elif you=="PAPER":
            return True
        else :
            return False
    elif random_num==2:
        if you=="ROCK":
            return False
        elif you=="PAPER":
            return None
        else:
            return True
    else:
        if you== "ROCK":
            return True
        elif you=="PAPER":
            return False
        else:
            return None

result=game(random_num,you)

if result== None :
    print("The Game is Tie")
elif result :
    print("You Won!!!")
else:
    print("You Lose!!")

print(f"The computer was {comp_input}")








