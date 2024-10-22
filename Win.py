import random
 def rock_paper_scissors():
   options=["rock","paper","scissors"]
   computer_choice=random.choice(options)
   player_choice=input("Enter rock or paper or scissors:").lower()
  if(player_choice not in options):
    print("Invalid Choice!,Please Choose a valid options from  rock or paper or scissors")
    return 
print(f"Computer choose:{computer_choice}")
if player_choice==computer_choice:
  print("No winner and It is Tie!")
elif(player_choice=="paper" and computer_choice=="rock") or \ (player_choice=="rock" and computer_choice=="scissors") or \ (player_choice=="scissors" and computer_choice=="paper"):
  print("You Win!!")
else:
  print("You Loss! and Computer Win!!")
