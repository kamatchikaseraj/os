n=input("enter a number")
a=0
b=0
while(n!=0):
    a=n%10
    b=b+a
    n=n//10
print "the sum of integer",b