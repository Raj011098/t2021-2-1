class calc:
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
z=calc
while True:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=int(input("[1]add [2]sub [3]mul [4]div\nenter:"))
    if c==1:
        z.add()
    elif c==2:
        z.sub()
    elif c==3:
        z.mul()
    elif c==4:
        z.div()
    else:
        print("invalid option")
