a=[1,2,8,9,12,46,76,82,15,20,30]
b=len(a)
d={}
for i in range(1,10):
    def func(x):
        if (x%i==0):
            return True
        else:
            return False
    n=list(filter(func,a))
    d.update({i:len(n)})
print(d)
