# ls =[]
# for i in range(100):
#     if i%2==0:
#         ls.append(i)
# print(ls)
lis= [i for i in range(100) if i%10==0]
print (lis)
dis = {i:f"Item {i}" for i in range(10) if i%2==0}
dis1 ={value:key for key,value in dis.items()}
print (dis,"\n",dis1)

st = {i for i in ["item1","item2","item1","item2"]}
print(st)
genrater = (i for i in range(10) if i%2==0)
for i in genrater:
    print(i)