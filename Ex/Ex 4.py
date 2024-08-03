number= int (input ("Enter The Number "))
bo = int (input ("Enter 0 or 1 "))
bol = bool(bo)
# print(bol)

if bol==True:
    for i in range(0,number):
        for j in range(i+1):
            print ("*",end="")
        print("")
elif bol == False:
    for i in range(number,0,-1):
        for j in range(i):
            print("*",end="")
        print("")