m = int(input("\nPlease Enter any Number: "))
l=[]
for j in range(0,100):
    if (j%2!=0):
        l.append(j)
if m>0:
    if (m%2!=0):
        print(l[0:m])
    else:
        print(l[0:(m-1)])
