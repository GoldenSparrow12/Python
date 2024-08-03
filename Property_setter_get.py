class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email = f"{fname}.{lname}@harcker.com"
    
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return("Enter email using setter method")
        return f"{self.fname}.{self.lname}@harcker.com"

    @email.setter
    def email(self,string):
        name=string.split("@")[0]
        self.fname= name.split(".")[0]
        self.lname= name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


e1= Employee("Harshit","Thumar")
print (e1.email)
e1.fname="jay"
print (e1.email)
e1.email="this.that@harcker.com"
print(e1.fname)
print(e1.lname)
print (e1.email)
del e1.email
print (e1.email)