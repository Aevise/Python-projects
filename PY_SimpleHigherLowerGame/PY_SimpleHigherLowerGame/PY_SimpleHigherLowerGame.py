from random import randint
from PY_SHLGameLogo import logo, vs
from PY_SHLDatabase import data

playGame = True
AFollowerCount = 0
BFollowerCount = 0
secondData = 0
decision = ""
gameOver = False

def getFollowerCount(data: dict, number: int) -> int:
    return data[number]['follower_count']

def format_data(data):
    data_name = data["name"]
    data_descr = data["description"]
    data_country = data["country"]
    return f"{data_name}, a {data_descr}, from {data_country}"

while playGame:

    playerScore = 0
    number = randint(0, (len(data)-1))
    while gameOver == False:
        print(logo)
        print("Compare A:", format_data(data[number]))
        AFollowerCount = data[number]["follower_count"]
        print(vs)
        VSNumber = number

        while VSNumber == number:
            VSNumber = randint(0, (len(data)-1))

        print(f"Against B:", format_data(data[VSNumber]))
        number = getFollowerCount(data, number)
        BFollowerCount = getFollowerCount(data, VSNumber)

        while True:
            decision = input("Who has more followers? Type 'A' or 'B': ").upper()
            if((decision != 'A') or (decision != 'B')):
                break
        
        if(decision == 'A' and AFollowerCount > BFollowerCount):
            playerScore += 1
            number = VSNumber
            print(f"You're right! Current score: {playerScore}")
        elif(decision == 'A' and AFollowerCount < BFollowerCount):
            print(f"Sorry, you are wrong. Final Score: {playerScore}")
            gameOver = True
        elif(decision == 'B' and AFollowerCount > BFollowerCount):
            print(f"Sorry, you are wrong. Final Score: {playerScore}")
            gameOver = True
        elif(decision == 'B' and AFollowerCount < BFollowerCount):
            playerScore += 1
            number = VSNumber
            print(f"You're right! Current score: {playerScore}")
            
    
    while True:
        decision = input("Try again? 'yes' or 'no': ").lower()
        if(decision == 'yes'):
            gameOver = False
            break
        elif(decision == 'no'):
            playGame = False
            break