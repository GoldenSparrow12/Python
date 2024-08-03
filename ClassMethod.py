class Employee:

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printsetails(self):
        print(f"Name Is {self.name} Salary is {self.salary} and Role is {self.role}")
    
    @classmethod
    def fun_dash(cls,string):
        # lis = string.split("-")
        # return cls(lis[0],lis[1],lis[2])
        return cls (*string.split("-"))

e1= Employee("Harshit",50000,"Manager")
e2= Employee("Deep",50000,"Manager")
e3 = Employee.fun_dash("Karan-45000-Employee")

e1.printsetails()
e2.printsetails()
e3.printsetails()