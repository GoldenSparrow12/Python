"""count how many charter in string"""


def frequent(str1):
    dict1 = {}
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in str1:
        if dict1[i] != 0:
            print(f"{i} is in {dict1[i]} time")
            dict1[i] = 0


if __name__ == '__main__':
    inp = input("Enter the string")
    frequent(inp)
