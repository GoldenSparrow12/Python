a = int(input())

for i in range(1, a ** 2):
    if i == 1 or i % a == 0:
        if i == 4:
            continue
        for j in range(1, a ** 2):
            print("* ",end="")

    else:
        for j in range(1, a ** 2):
            if j == 1 or j % a == 0:
                print(" *",end="")
            else:
                print("  ",end="")
    print("\n")
