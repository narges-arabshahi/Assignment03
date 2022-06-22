
import random
n=[]
list=int(input("Please enter n: "))
for i in range(list):
   a=random.randint(0,1000+list)
   if a not in n:
    n.append(a)
print(n)
