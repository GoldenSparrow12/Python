
n = int ( input ("Enter the number") )

def fact(n):

        f=1
        for i in range(1,n+1):
                f=f*i
        print(f)        

if(n>0):
        fact(n)
else:
        print("Invalid Number")
                
