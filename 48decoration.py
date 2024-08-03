# f= lambda a,b:print(a/b)

# def div1(fun):

#         def funs(a,b):
#                 if a<b:
#                         a,b =b,a
#                 return fun(a,b)
#         return funs
# f=div1(f)
        
# a= int (input ("Enter 1 element "))
# b= int( input ( "Enter 2 element"))
# f(a,b)

def dec(fun):
        print("Starrt")
        fun()
        print ("End")
@dec
def ha():
        print ("this is ha")


ha() 