
def add(x,y):
    s=x+y
    print("addition of",x ,"and",y,"is=",s)
def sub(x,y):
    s=x-y
    print("the subtraction of",x,"and",y,"is =",s)
def mul(x,y):
    s=x*y
    print("multiplication of",x,"and",y,"is =",s)
def div(x,y):
        s=x//y
        print("the result is:",s)
def mod(x,y):
    s=x%y
    print("the mod division of ",x,"and",y,"is=",s)

print("**********-----------**************")
print("1.addition/n/n2.subtraction/n/n/n3.multiplication/n/n/n4.division/n/n/n5.mod division ")
print("**************                   ************")
x=int(input("enter x value:"))
y=int(input("enter y value:"))
ch=int(input("enter your choice:"))
if ch==1:
     add(x,y)
elif ch==2:
     sub(x-y)
elif ch==3:
     mul(x,y)
elif ch==4:
     div(x,y)
elif ch==5:
     mod(x,y)
else:
     exit     
