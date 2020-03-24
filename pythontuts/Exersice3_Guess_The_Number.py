i=0
j=int(5)
a=18
print("Guess the number guys,toatal guesses=5")

while(j>0):
    k = int(input("Enter any Number"))
    if k==a:
        print("You Won")
        break
    elif k>a:
        print("Try smaller number")
    elif k<a:
        print("Try bigger number")
    j = j - 1
    print("Guesses left",j)
print("Game Over")



