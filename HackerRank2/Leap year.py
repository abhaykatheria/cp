def year(n):
    if n%4==0 and n!=1700 and n!=1800 and n!=1900:
        if n%100==0 and n%400!=0:
            print("13.09."+str(n))
        elif n%400==0:
            print("12.09."+str(n))
        else:
            print("12.09."+str(n))
    else:
        if n==1918:
            print("26.09.1918")
        else:
            if n==1700 or n==1800 or n==1900:
                print("12.09."+str(n))
            else:
                print("13.09."+str(n))

n=int(input())
year(n)