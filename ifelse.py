x=int(input("Enter 1 number"))
y=int (input("Enter 2 number"))
z=int (input("Enter 3 number"))
if(x>y):
        if(x>z):
                print("1 number is greater")
                print(x)
        else:
                print("3 number is greater")
                print(z)
if(y>x):
        if(y>z):
                print("2 number is greater")
                print(y)
        else:
                print("3 number is greater")
                print(z)
if(x==y==z):
        print("All Are equle")

