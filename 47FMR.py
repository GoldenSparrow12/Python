from functools import reduce
# lis = []

# n= int ( input ("Enter the number in list "))
# for i in range(n):
#         ele= int(input())
#         lis.append(ele)
# print(lis)
# even = list( filter (lambda n:n%2==0,lis))
# print(even)
# add = list ( map (lambda n:n+2,lis))
# print (add)
# sums = reduce(lambda a,b:a+b,even)
# print(sums)

lis =[1,2,3,4,5,6,7,8,9,10]
map1 = list(map(lambda a:a*a,lis))
print (map1)
filter1 = list(filter(lambda a:a%2==0,lis))
print(filter1)
reduce1 = reduce(lambda a,b:a+b ,lis)
print(reduce1)