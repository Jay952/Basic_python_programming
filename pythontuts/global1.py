l=10
def function1(n):
    l=8
    m=5
    global l
    l=l+90
    print(l,m)
    return print(n,"I have printed")

function1("Calling function and sending this line")
