import random 
print ("Welcome to the Rock, Paper, Scissors game!")
options =["ROCK", "PAPER", "SCISSORS"]
user = input ("enter your choice ").upper()
computer= random .choice(options)
print("you choose :", user)
print("Computer choose :", computer)

# comparing the choices
if user == computer:
    print ("It's a tie!")
elif (user == "ROCK" and computer == "SCISSORS"):
  print("You win!")

elif (user == "PAPER" and computer == "ROCK"):
  print ("You win!")
elif(user == "SCISSORS" and computer == "PAPER"):
    print ("You win!")


elif (computer == "ROCK" and user == "SCISSORS"):
    print ("Computer wins!")    
elif (computer == "PAPER" and user == "ROCK"):
    print ("Computer wins!")
elif (computer == "SCISSORS" and user == "PAPER"):
    print ("Computer wins!")

else:
 print("invalid input ")
