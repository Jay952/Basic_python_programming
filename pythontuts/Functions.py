a=5
b=8
c=sum([a,b])
print(c)

def function1(a,b):
    print("You are in function1",a+b)
print(function1(9,8))
function1(9,9)

def function2(a,b):
    print("You are in function2")
    c=(a+b)/2
    print(c)

function2(5,7)


def function3(m,n):
    """This is function which contains if else and not work for three numbers"""
    if m>n :
        return m+n;
    else:
        return m-n;

print(function3(5,6))

print(function3.__doc__)





