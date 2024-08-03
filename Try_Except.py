i1= input("Enter 1 number")
i2= input("Enter 2 number")

try:
    print ("Division is",
           int(i1)/int(i2))
except ValueError as e:
    print("Invalid Input ")
except ZeroDivisionError as e:
    print("Not Divide By Zero")
else:
    print("No Error Doing..")
finally:
    print("All operation done")
