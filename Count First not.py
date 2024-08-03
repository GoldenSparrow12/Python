def countstr(str1):
    dict1 = {}
    f_not_r = []

    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            f_not_r.append(i)
    for i in f_not_r:
        if dict1[i] == 1:
            print(i, end=" ")


if __name__ == '__main__':
    int1= input("Enter The string")
    countstr(int1)
