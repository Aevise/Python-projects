from random import randint

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

availableChoices = [Rock, Paper, Scissors]
yourChoice = 0
yourScore = 0
AIChoice = 0
AIScore = 0


while True:
    yourChoice = int(input("Choose wisely. Rock = 0, Paper = 1, Scissors = 2\nMy choice is "))
    AIChoice = randint(0, (len(availableChoices)-1))
    print(f"Your choice:\n{availableChoices[yourChoice]}")
    print(f"AI choice:\n{availableChoices[AIChoice]}")
    if (yourChoice == AIChoice):
        print("DRAW!")

    if(yourChoice == 0 and AIChoice == 1):
        print("AI Wins!")
        AIScore += 1
    elif(yourChoice == 0 and AIChoice == 2):
        print("Player Wins!")
        yourScore += 1
    elif(yourChoice == 1 and AIChoice == 0):
        print("Player Wins!")
        yourScore += 1      
    elif(yourChoice == 1 and AIChoice == 2):
        print("AI Wins!")
        AIScore += 1
    elif(yourChoice == 2 and AIChoice == 0):
        print("AI Wins!")
        AIScore += 1
    elif(yourChoice == 2 and AIChoice == 1):     
        print("Player Wins!")
        yourScore += 1         
           
    print(f"Current Score: Player: {yourScore}, AI: {AIScore}")
