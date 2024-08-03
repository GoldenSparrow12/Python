n = int(input("Enter the value "))
g = 10000


def fibo(n):
    a, b = 0, 1
    if n == 0:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, g):
            c = a + b
            a, b = b, c
            if c > n:
                break
            print(b)


fibo(n)
