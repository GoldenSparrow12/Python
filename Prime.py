x=int (input("Enter A Number "))
for i in {2,3,5}:
        if(x==i):
                print("Prime")
                break
        elif(x%i == 0):
                print("Not Prime")
                break
else:
        print("Prime")
