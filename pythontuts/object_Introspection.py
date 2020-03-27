class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{self.fname}.{self.lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname= names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None

skillf=Employee("Skill","F")
print(skillf.email)

# print(type(skillf))
# print(type("Jaydeep"))
# print(id("jaydeep"))
# print(id("Chawda"))
# o="This is a string"
# print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))
