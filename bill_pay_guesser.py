import random

string= input("Enter the number of the person who want to pay bill : ")

arr=string.split()

lenght=len(arr)-1

rand=random.randint(0,lenght)

print(f"{arr[rand]} is selected to pay the bill ")

