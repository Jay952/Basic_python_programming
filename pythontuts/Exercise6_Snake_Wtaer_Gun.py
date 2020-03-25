import random
lst1=["Snake","Water","Gun"]

print("You will play three Times!!\n")

k=0
computer=0
yourscore=0
while(k<3):
    com = random.choice(lst1)
    me = input("Enter your choice Snake,Water,Gun:")
    if com == 'Snake':
        if me == 'Gun':
            print("You won")
            yourscore=yourscore+1
        elif me == 'Snake':
            print("Draw")
        else:
            print("You Lose")
            computer=computer+1
    elif com == 'Water':
        if me == 'Gun':
            print("You Lose")
            computer = computer + 1
        elif me == 'Snake':
            print("You Won")
            yourscore = yourscore + 1
        else:
            print("Draw")
    else:
        if me == 'Gun':
            print("Draw")
        elif me == 'Snake':
            print("You Lose")
            computer = computer + 1
        else:
            print("You Won")
            yourscore = yourscore + 1
    k=k+1
if(yourscore>computer):
    print("You are a winner",f"{yourscore}:{computer}")
else:
    print("you are a Loser",f"{yourscore}:{computer}")
