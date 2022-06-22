n=int(input("Please enter n: "))
for i in range(n):
    if i % 2 == 0:
        print("*",end=" ")
    else:
        print("#",end=" ")

    