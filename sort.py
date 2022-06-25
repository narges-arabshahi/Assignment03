number=[]
m=""
while True:
    x=int(input("Please enter number or -1 to exit: "))
    if x==-1:
        break
    else:
        number.append(x)
    j=number[0]
print(number)
for i in range(1,len(number)):
    if j>number[i]:
        m="array is not sort"
        print(m)
        break
    else:
        j=number[i]
if m=="":
    print("array is sort")
