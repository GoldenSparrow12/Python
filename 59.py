class A:
    def name(self):
        print ("Harshit")

    def surname(self):
        print("Thumar")

class B():
    def lastname(self):
        print ("M")

class C(A,B):
    def prin(self):
        self.name()
        self.surname()
        self.lastname()

c=C()
c.prin()