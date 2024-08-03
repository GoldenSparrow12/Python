class Employe():
    def __init__(self,name,salary,inty,role):
        self.name= name
        self.salary=salary
        self.inty =inty
        self.role= role

    def printdetail(self):
        return print(f"Name is {self.name},Salary is {self.salary},Role is {self.role}")

    def __add__(self,other):
        self.m1= self.inty + other.inty
        self.m2= self.salary + other.salary
        return self.m1,self.m2


    def __str__(self):
        return f"Name is {self.name},Salary is {self.salary},Role is {self.role}"

    def __gt__(self,other):
        if self.salary > other.salary:
            print (f"Salary are greater {self.name}")
        else:
            print (f"Salary are greater {other.name}")

E1=Employe('Harshit',50000,600,'CEO')
E2=Employe('Deep',400000,700,'Manager')

E3= E1 + E2
E4 =E1>E2
print(E3)

print(E1)

print (E2)