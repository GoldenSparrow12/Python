n = int(input("Enter the number "))


def fibo(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a, b = b, c
            print(c)


if n < 0:
    print("Invalid Number")
else:
    fibo(n)
