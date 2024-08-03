def fibo(number):
    a=0
    b=1
    if number==1:
        print(0)
    elif number==2:
        print(0,1)
    else:
        print (0)
        print(1)
        for i in range(2,100):
            c=a+b
            a,b=b,c
            if b>=number:
                break
            print (c)

number= int (input(""))
fibo(number)
        