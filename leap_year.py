# leap year checker

n=int(input("Enter the year you want to check : "))

if(n%4==0):
    if(n%100==0) :
        if(n%400==0):
            print(f"{n } is a leap year")
        else :
            print(f"{n } is not a leap year")
    print(f"{n } is a leap year")
else :
    print(f"{n } is not a leap year")
