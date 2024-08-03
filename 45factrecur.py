
n= int ( input ("Enter The number"))
def fact(n):

        if(n==0):
                return 1

        return n* fact(n-1)
        
if (n>=0):
        result = fact(n)
        print(result)
else:
        print ("Invalid Number")
