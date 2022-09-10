from random import choice
from PY_Hangman2Art import stages, logo
from PY_Hangman2Words import listOfWords

numberOfWords = len(listOfWords) - 1
chosenWord = choice(listOfWords)

playerList = []
chosenLetter = ""
history = []
completedWord = ""
playerLives = len(stages) - 1

print(logo, "\nTo feed or to be devoured that is the question\n")

for _ in chosenWord:
    playerList.append("_")
    #mozna to tez zrobic tak playerList += "_"
while ((completedWord != chosenWord) and (playerLives != 0)):
    completedWord = ""
    iterator = 0
    chosenLetter = str(input("Please type in a letter: ")).lower()
    if(chosenLetter in history):
        print("You have already picked this letter. Try again")
    else:
        history.append(chosenLetter)
        if (chosenLetter in chosenWord):
            print("Congratulation you have found a letter on na position:", end = "")
            for letter in chosenWord:
                if(letter == chosenLetter):
                    playerList[iterator] = chosenLetter
                    print(f" {iterator+1}", end = "")
                iterator += 1
            print(".")
        else:
            print(f"Chosen letter '{chosenLetter}' is not found in the selected word")
            playerLives -= 1
    completedWord = completedWord.join(playerList)
    print(stages[playerLives])
    print(completedWord)

if(playerLives != 0):

    print(f"\nCongratulations. You have won and opportunity to feed {chosenWord.capitalize()}")
else:
    print(f"\nYou are going to be fed to {chosenWord.capitalize()}")