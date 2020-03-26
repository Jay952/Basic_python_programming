class Employee:
    number_of_leaves=8
    pass
harry=Employee()
rohan=Employee()
harry.name="Harry"
harry.salary=5000
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=10000
rohan.role="Student"

rohan.number_of_leaves=11
print(rohan.salary)
print(rohan.__dict__)
print(harry.__dict__)
print(harry.number_of_leaves)
