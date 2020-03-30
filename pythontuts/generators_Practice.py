
n=int(input("Enter Value of 'n':"))


def gen(n):
    for i in range(n):
         yield i
g=gen(n)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

def Fact(n):
    if n==1:
        yield 1
    else:
        yield n

w=Fact(n)
print(w.__next__())
print(w.__next__())
print(w.__next__())
print(w.__next__())