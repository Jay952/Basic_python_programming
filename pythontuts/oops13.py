class A:
    def met(self):
        print("This is method from class A")

class B(A):
    def met(self):
        print("This is method from class B")

class C(A):
    def met(self):
        print("This is method from class C")

class D(C,B):
    pass

a=A()
b=B()
c=C()
d=D()
print(a.met())
print(d.met())