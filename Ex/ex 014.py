
lst =[1,5,54,1521,895,10,50]
new_lst =[]
for i in lst:

    if i<10:
        new_lst.append(i)
        continue
    else:
        while str(i) != str(i)[::-1]:
            i +=1
        new_lst.append(i)
print(new_lst)