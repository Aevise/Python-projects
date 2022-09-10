############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from PY_BlackjackLogo import logo
import random

def drawCard(cards: list) -> int:
    """
    Functions that draw cards from the deck. 
    Cards have equal probability to be drawn.
    Cards are not removed from the deck
    """
    return random.choice(cards)

def AceDecide(cards: list, IsPlayer = True) -> int:
    """
    Function responsible whether you want to count your Ace as 1 or 11
    IsPlayer = False means AI decides how to count drawn Ace
    """
    while True:
        if(IsPlayer):
            value = int(input("Do you want to count your Ace as 1 or 11? As: "))
            if(value == 1 or value == 11):
                return value
            else:
                print("Incorrect Value")
        else:
            if(sum(cards) > 21):
                return 1
            else:
                return 11
        

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerScore = []
playerCash = 1000
dealerScore = []
decision = ""
playGame = True

print(logo)
while playGame:
    print("Drawing cards....")
    for _ in range (2):
        playerScore.append(drawCard(cards))
        dealerScore.append(drawCard(cards))       
    print(f"Dealer's score is equal to: {dealerScore[0]}")
    print(f"Your cards are: {playerScore}. Your score is {sum(playerScore)}.")
    for card in range(0, len(playerScore)):
        if(playerScore[card] == 11):
            playerScore[card] = AceDecide(playerScore)
    
    while True:
        decision = str(input("Do you want to draw a card? yes or no. Decision: ")).lower()
        if(decision == "yes"):
            playerScore.append(drawCard(cards))
            if(playerScore[-1] == 11):
                playerScore[-1] = AceDecide(playerScore)
            if(sum(playerScore) > 21):
                break
            print(f"Your cards are: {playerScore}. Your score is {sum(playerScore)}.") 
        elif(decision == "no"):
            break

    while((sum(dealerScore) < 17) and (sum(playerScore) < 21)):
        dealerScore.append(drawCard(cards))
        if(dealerScore[-1] == 11):
            dealerScore[-1] = AceDecide(dealerScore, False)

    print(f"Your cards are: {playerScore}. Dealer's cards are: {dealerScore}")
    if(sum(playerScore) > 21):
        print("Player's Bust. Dealer wins.")
    elif(sum(dealerScore) > 21):
        print("Dealer's Bust. Player wins")
    elif(sum(playerScore) > sum(dealerScore)):
        print("Player wins")
    elif(sum(playerScore) < sum(dealerScore)):
        print("Dealer wins")
    else:
        print("Draw")

    while True:
        decision = str(input("Do you want to play again? yes or no. Decision: ")).lower()
        if(decision == "yes"):
            playerScore.clear()
            dealerScore.clear()
            break
        elif(decision == "no"):
            playGame = False
            break