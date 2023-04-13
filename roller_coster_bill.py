#roller coster 

height=int (input("Enter your height in cm : " ))

price=0
age=0

if(height>=120):
    age=int(input("Enter your age : "))

    if(age<12):
        price+=5
    elif(age>=12 and age<=18):
        price+=7
    elif(age>18 and age<45):
        price+=12
    else:
        price+=0
    photo=input("would you like to take photo if yes press y else n")

    if(photo=="y"):
        price+=3

    print(f"your toatal bill is {price }")



else :
    print("sorry you can't ride your height is less than 120 cm ")
