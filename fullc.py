yrs=int(input("enter the year:"))
start = 1
pos = 1
if yrs%4==0:
    leap=1
    print("leap")
else:
    leap=0
    print("not")
month = ["January", "Feburary", "March", "April", "May", "June","July","August","September","October","November","December"]
for  m in range(len(month)):
    print
    print ("%8s" % month[m])
    i=m+1
    week = ["sun", "mon", "tues", "wed", "thu", "fri","sat"]
    for  days in range(len(week)):
        print ("%8s" % week[days]),
    print
    if(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12)and (leap==0 or leap==1):
        days = 32
    if(i==4 or i==6 or i==9 or i==11)and (leap==0 or leap==1):
        days = 31
    if i==2 and leap==1:
        days = 30
    if i==2 and leap==0:
        days = 29
    while (pos<start):
        print ("%8s" % " "),
        pos = pos+1
        start=start+1
    for i1 in range(1,days):
        if (pos % 7 >=1 and pos%7 <= 6):
            print ("% 8d" % i1),  
            pos = pos+1
            start=start+1
        elif pos %7 == 0:
            print ("%8d" %i1)
            pos = pos+1
            start=start+1
            

