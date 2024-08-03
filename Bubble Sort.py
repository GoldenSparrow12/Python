n= int(input("Enter the list number"))

print("Enter The List")
lis=[]
for i in range(n):
    inp = input()
    lis.append(inp)
print(lis)


def sort(lis):
    for i in range(len(lis)-1):
        for j in range(0,n-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]


sort(lis)
print(lis)