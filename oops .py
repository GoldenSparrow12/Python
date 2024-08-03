class Employee:
    """This is the Employee class which derive the Employee details"""
    comp_name = "Python"
    def __init__(self, name , salary ,role):
        self.name =name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        print (f"Employee Name Is {self.name},Salary is {self.salary} and the Role is {self.role} ")
    
    @classmethod
    def convert(cls,string):
        return cls (*string.split("-"))
    
    @staticmethod
    def gole():
        print ("This is the python programmer Job")

class Player(Employee):
    """This is the Player class which derive the player details"""
    def __init__(self,name,salary,role,game):
        super().__init__(name,salary,role)
        self.name=name
        self.game = game
    
    def printdetails(self):
        print (f"Employee Name Is {self.name},Salary is {self.salary} and the Role is {self.role} And The game is play {self.game}")

class CoolEmployee(Player):
    pass

e1=Employee("Harshit",100000,"Manager")
e2=Employee.convert("Deep-75000-Co.Manager")
p1=Player.convert("Harshit-100000-Manager-PUBG")
p2=Player.convert("Deep-75000-Co.Manager-PUBG")
c1=CoolEmployee.convert("Harshit-100000-Manager-PUBG")
c1.gole()
c1.printdetails()
