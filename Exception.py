
eg = int(input("Enter the Age"))
try:
    if eg < 18:
        raise ValueError("Massage")
    else:
        print(eg)
except ValueError as e:
    print("Not vaild", e)
