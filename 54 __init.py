
class cal():
        def __init__(self,name,age):
                self.name=name
                self.age=age
        def printit(self):
                print ("Name Is {} And Age {}".format(self.name,self.age))

c1 = cal('Harshit',20)
c2 = cal('Deep',20)

c1.printit()
c2.printit()
