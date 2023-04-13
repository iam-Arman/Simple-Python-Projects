#tip calculator

print("\t\t\t\t\t WELCOME TO TIP CALCULATOR")   

print("What is your totol bill $ : ")

bill = float(input())

print("What is percentage % tip you would like to give : ")

tip=int(input())

print("How many people you would like to split the bill :")

count=int(input())

pay_amount=(bill+((tip/100)*bill))/count

pay_amount=round(pay_amount,2)

pay_amount="{:.2f}".format(pay_amount)


print(f"each person should pay {pay_amount} $")

