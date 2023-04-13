import random

print("\t\t\t\t\t ____________ROCK     PAPER     SCISSOR__________\n\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

chose=int(input("ENTER 0 for rock , 1 for paper and 2 for scissor :  "));

arr=[rock,paper,scissors];

random=random.randint(0,2);

if(chose<0 or chose>2):
    print("Wrong input");
else:

 print(f"you chose {arr[chose] }\n");

 print(f"computer chose{arr[random]}\n");

 if(chose==0 and random==2):
    print("You win");
 elif(chose==1 and random==0):
    print("YOU WIN ");
 elif(chose==2 and random==1):
    print("YOU WIN");
 elif(chose==0 and random==1):
    print("YOU LOSE");
 elif(chose==2 and random==0):
    print("YOU LOSE");
 elif(chose==1 and random==2):
    print("YOU LOSE");
 else :
    print("GAME DRAW");


      
