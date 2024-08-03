def topten():

    n=1
    while(n<=10):
        sq=n*n*n
        yield sq
        n+=1

valus = topten()
for i in valus:
    print(i)