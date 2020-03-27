#private
#public
#protected



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


class programmer(Employee):
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage

    def printprog(self):
        return f"Programmers name is {self.name}.Salary is {self.salary}.And role is {self.role} and LAnguage is {self.language}"


class player:
    var = 99
    number_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Player name is {self.name}.Game is {self.game}."


class coolProgrammer(Employee, player):
    language = "C#"

    def printlanguage(self):
        print(self.language)


rohan = Employee("Rohan", 5000, "Insructor")
harry = Employee("Harry", "10000", "Student")

shubham = coolProgrammer("Shubham", 90000, "coolProgrammer")
# print(shubham.printdetails())
# #
# # shubham.printlanguage()
# print(shubham.var)
print(rohan._protected)
print(rohan._Employee__private)