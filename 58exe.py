class Student:

    def __init__(self,name,roll,branch):
        self.name = name
        self.roll = roll
        self.branch= branch
    
    def show(self):
        print (self.name,self.roll,self.branch)


    class Laptop:
        def __init__(self,lap,cpu,ram):
            self.lap =lap
            self.cpu= cpu
            self.ram =ram

        def show(self):
            print(self.lap,self.cpu,self.ram)
            
s1= Student('Harshit',112,'Com',)
s2= Student('Deep',44,'Com')

lap1 = Student.Laptop('HP','i5',8)
lap2 = Student.Laptop('Lanova','i3',4)

s1.show()
lap1.show()
s2.show()
lap2.show()