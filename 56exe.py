class School:
    name = "SAL"

    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        
    def info(self):
        return (self.s1 +self.s2 + self.s3)/3

    @staticmethod
    def sub_name():
        name1 = "Computer"
        return name1

    @classmethod
    def classme(cls):
        cls.division = "A"
        return cls.division

s1=School(90,90,90)
s2=School(80,80,80)
School.division ="B"

print (School.name,School.sub_name(),School.classme(),s1.info())
print (School.name,School.sub_name(),School.classme(),s2.info())
