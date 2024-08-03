
arr = [1,2,3,4,5,6,7,8,9]
nu = int (input("Enter the number which you Search"))
pos = 0
# linear Search useing loop
# for i in arr:
#     if i==nu:
#         pos = pos+1
#         print("Found at",pos)
#         break
# else:
#     print("Not Found")

# Linear Search using function
def search(list,number):
    """This function is use for linear search"""
    for i in list:
        global pos
        pos = pos+1
        if i == number:
            return True
    else:
        return False


if search(arr,nu):
    print("Found at",pos)
else:
    print("Not Found")