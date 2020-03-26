class Employee:
    number_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary}.And role is {self.role}"

rohan=Employee("Rohan",5000,"Insructor")
harry=Employee("Harry","10000","Student")



# harry.name="Harry"
# harry.salary=5000
# harry.role="Instructor"
#
# rohan.name="Rohan"
# rohan.salary=10000
# rohan.role="Student"

print(harry.printdetails())

