def sam(a,b):
        c=a+b
        print(c)
def sub(a,b):
        c=a-b
        print(c)
def mul(a,b):
        c=a*b
        print(c)        
def div(a,b):
        c=a/b
        print(c)
print(" 1.Add\n 2.Subtract\n 3.Multiple\n 4.Division\n 5.Exit")
n = int(input("Enter the operation "))
while(n != 5):        
        print(" 1.Add\n 2.Subtract\n 3.Multiple\n 4.Division\n 5.Exit")


  
        a= int ( input ("Enter the 1 number "))
        b= int ( input ("Enter the 2 number "))

        if( n == 1):
                sam(a,b)
        elif( n == 2):
                sub(a,b)
        elif( n == 3):
                mul(a,b)
        elif( n == 4):
                div(a,b)
        else:
                print(" Wrong Input ")
