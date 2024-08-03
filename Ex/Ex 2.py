print ("Enter the opration you want")
print ("1.Add\n2.Substraction\n3.Multification\n4.Division")
op = int(input())
i1 = int (input ("Enter The 1 Number:"))
i2 = int (input ("Enter the 2 Number:"))

if op==1 and i1==56 and i2==9:
    print("77")
elif op==3 and i1==45 and i2==3:
    print ("555")
elif op==4 and i1==56 and i2==6:
    print ("4")
elif op==3:
    print (i1*i2)
elif op==1:
    print (i1+i2)
elif op==4:
    print (i1/i2)   
elif op==2:
    print (i1-i2)
else:
    print("Invaild Opration")