def print2(str1):
    return print("This is " + str1)

print2("Jaydeep")

n=int(input("Enter the number for factorial"))
def fact(k):
    if k==1:
        return 1

    else:
        return k*fact(k-1)
print(fact(n))

def fact1(l):
    f=1
    for i in range(l):
        f=f*(i+1)
    return f

print(fact1(n))

def fibo(j):
    if j==1 or j==0:
        return 1
    else:
        return fibo(j-1)+fibo(j-2)

print(fibo(n))








