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

    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good "+string)
        return 0


rohan=Employee("Rohan",5000,"Insructor")
harry=Employee("Harry","10000","Student")
karan=Employee.from_str("Karan-15000-Student")
print(karan.salary)

rohan.changeleaves(54)
print(harry.printgood("Jaydeep"))