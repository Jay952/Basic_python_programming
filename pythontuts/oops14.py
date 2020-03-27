
class Employee:
    var = 10
    number_of_leaves = 9
    _protected=442
    __private=99

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary}.And role is {self.role}"

    @classmethod
    def changeleaves(cls, newleaves):
        cls.number_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return 0
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary/other.salary
    def __repr__(self):
        return self.printdetails()
    def __str__(self):
        return  f"{self.salary},{self.name},{self.role}"

emp1=Employee("Harry",5000,"Student")
emp2=Employee("Rohan",3000,"Cleaner")

print(emp1.salary)
print(emp1+emp2)
print(emp1/emp2)

print(emp1)