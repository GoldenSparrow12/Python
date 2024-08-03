def count(lst):
        more=0
        less=0
        for i in lst:
                if(len(i)<5):
                        less+=1
                else:
                        more+=1
        return more,less                
lst = []
n= int( input("Enter the number of element "))
for i in range(0,n):
        ele=input()
        lst.append(ele)

more,less =count(lst)
print("Greter Then 5 : {} , Less Then 5 : {}".format(more,less))
