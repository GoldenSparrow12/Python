f= open("Harshit.txt","rt")
content = f.read()
# print (content)
for line in content:
    print(line,end="")
# for line in f:
#     print (line,end="")
# print (f.readline())
# print (f.readline())
# print (f.readline())
# print (f.readlines())

f.close()
# with open("Harshit.txt") as f:
#     print(f.read())