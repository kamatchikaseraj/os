def day(n,m):
    if(n<=12):
        if(m%4==0):
            if(n==2):
                print("There are 29 days in a month")
            else:
                if(n==1 or n==3 or n==5 or n==7 or n==9 or n==11 or n==12):
                    print("There are 31 days in a month")
                else:
                    print("There are 30 days in a month")
        else:
            if(n==1 or n==3 or n==5 or n==7 or n==9 or n==11 or n==12):
                print("There are 31 days in a month")
            else:
                print("There are 30 days in a month")

n=input("enter the month:")
m=input("enter the year:")
day(n,m)