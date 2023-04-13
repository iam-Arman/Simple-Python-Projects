#Love Calculator

print("\t\t\t\t\t -----------WELCOME CALCULATE YOUR LOVE------------ \n")

name1=input("Enter person 1 name : ")
name1=name1.lower()

name2=input("Enter person 2 name : ")
name2=name2.lower()

concated_name=name1+name2

count_1st=int(concated_name.count("t"))+int(concated_name.count("r"))+int(concated_name.count("u"))+int(concated_name.count("e"))
count_2nd=int(concated_name.count("l"))+int(concated_name.count("o"))+int(concated_name.count("v"))+int(concated_name.count("e"))

love=str(count_1st)+str(count_2nd)
love=int(love)

if(love<10 or love>90) :
    print(f"Your score is {love } , You go together like coke and mentos ")
elif(love>=40 and love<=50):
    print(f"your score is {love }, you are all right together ")
else :
    print(f"Your score is {love }")
