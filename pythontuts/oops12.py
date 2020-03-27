class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A constructor"
        self.classvar1="Instance var in class A"
        self.special="Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):

        self.var1="I am in classs B constructor"
        self.classvar1=" Instance var in class B"
        super().__init__()


a=A()
b=B()
print(b.var1)