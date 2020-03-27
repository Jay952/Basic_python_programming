
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




hindustani_supporter=Employee("Hindustani","Supporter")
nikhil_raj_pandey=Employee("Nikhil","Raj Pandey")
# print(hindustani_supporter.explain())
#
# print(hindustani_supporter.printemail)
#
# hindustani_supporter.fname="US"
#
# print(hindustani_supporter.printemail)

hindustani_supporter.email="this.that@codewithharry.com"

print(hindustani_supporter.lname)
del hindustani_supporter.email

print(hindustani_supporter.email)
