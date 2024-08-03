
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,1552]
nu = int(input("Enter the number which you Search"))
pos = 1


def search(list,number):
    l = 0
    u = len(arr)-1

    while l <=u:
        mid = (l + u) // 2
        global pos
        pos = mid+1
        if list[mid] == number:
            return True
            break
        else:
            if list[mid] < number:
                l=mid+1
            else:
                u=mid-1
    return False


if search(arr,nu):
    print("Found at", pos)
else:
    print("Not Found")
