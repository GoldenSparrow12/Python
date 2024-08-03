
class Invalid(Exception):
    def __init__(self,string):
        self.string=string

    def __str__(self):
        return repr(self.string)


eg = int(input("Enter the Age"))
try:
    if eg < 18:
        raise Invalid("Massage")
    else:
        print(eg)
except Invalid as e:
    print("Not vaild", e.string)
