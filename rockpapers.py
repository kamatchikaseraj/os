print "rock paper scissors"
n=raw_input("enter first user")
m=raw_input("second user")
if(n==m):
    print "draw"
elif((n=="rock")and (m=="scissors")):
    print "n is winner"
elif ((n=="scissors")and(m=="rock")):
    print "m is winer"
        