# ls =[]
# i=int(input ("Enter the number of element "))
# for j in range(i):
#     k=input()
#     ls.append(k)
# print (ls)
inr = eval(input())
ch= eval(input ('Press\n'
                '1 for list Co\n'
                '2 for dictionary Co\n'
                '3 for set Co\n') )
if ch==1:
    lis = ['i am' for i in range(inr)]
    print(lis)
elif ch==2:
    dic={i:f"i am {i}" for i in range(inr) }
    print(dic)
elif ch==3:
    sets ={'i am' for i in range(inr)}
    print(sets)