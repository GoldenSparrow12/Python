n= int(input("Enter the list number"))

print("Enter The List")
lis=[]
for i in range(n):
    inp = input()
    lis.append(inp)
print(lis)


def Selsort(lis):

    for i in range(n):
      min = i
      for j in range(i+1,n+1):
          if lis[j]<lis[min]:
              min = j
      lis[i],lis[min]=lis[min],lis[i]
    print(lis)

Selsort(lis)
print(lis)