class Student:
    def __init__(self,name,age,std):
        self.name= name
        self.age = age
        self.std = std 
    def printde(self):
        print(f"Name Is {self.name},Age Is {self.age},Std {self.std}")

harshit = Student("Harshit",20,"7 Sem")
deep = Student("Deep",28,"7 Sem")


# harshit.name = "Harshit"
# harshit.age = 20
# harshit.std ="7 Sem"

# deep.name="Deep"
# deep.age = 20
# deep.std ="7 Sem"

harshit.printde()
deep.printde()