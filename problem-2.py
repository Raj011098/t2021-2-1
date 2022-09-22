m = int(input("\nPlease Enter any Number: "))
l=[]
for j in range(0,100):
    if (j%2!=0):
        l.append(j)
print(l[0:m])
