class Employee:
    number_of_leaves=9
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary}.And role is {self.role}"
    @classmethod
    def changeleaves(cls,newleaves):
        cls.number_of_leaves=newleaves


rohan=Employee("Rohan",5000,"Insructor")
harry=Employee("Harry","10000","Student")
rohan.changeleaves(54)
print(harry.number_of_leaves)