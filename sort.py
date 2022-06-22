number=[]
x=int(input("Please enter n: "))
for i in range(x):
    user=int(input("Please enter number: "))
    number.append(user)
    number.sort()
print(number)