def function1():
    print("subscribe Now")

Func2=function1
del function1
Func2()
def funcret(num):
    if num==0:
        return print("I am Jaydeep")
    if num==1:
        return int(5)

a=funcret(0)
print(a)

def executor(func):
    func("this")

executor(print)

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec
@dec1
def jay():
    print("Jaydeep is Hard working Boy")

# jay=dec1(jay)
jay()
