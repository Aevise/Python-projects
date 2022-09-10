from http.cookiejar import LWPCookieJar
import random

#
def is_Encounter(encounter_chance = 60):
    if (random.randint(0,100) <= encounter_chance):
        return True
    else:
        return False

def mixed_Rewards(value):
    lowestValue = value - (0.1*value)
    highestValue = value + (0.1*value)
    return random.randint(lowestValue, highestValue)


def reward_from_Chest(types_of_chests, green_reward = 1000, yellow_reward = 4000, violet_reward = 9000, golden_reward = 1600):
    rolled_chest = random.choices(types_of_chests, [75, 20, 4, 1])
    reward = types_of_chests.index(rolled_chest[0])
    
    if (reward == 0):
        print("You have found a common green chest")
        return green_reward
    elif (reward == 1):
        print("You have found a rare yellow chest")
        return yellow_reward
    elif (reward == 2):
        print("You have found an epic violet chest")
        return violet_reward
    elif (reward == 3):
        print("You have found a legendary golden chest!!!")
        return golden_reward
    else:
        print("Something went terribly wrong")
        return 0


if __name__ == '__main__':
    gameLength = 5                                      #number of rolls
    hoarded_gold = 0                                    #amount of stashed gold
    chests = ['green', 'yellow', 'violet', 'golden']    #types of chests
    try: #checking if the player press something else than an number
        custom_game = int(input("If you want to play a standard game press 0. For custom game press something else\n"))
    except ValueError:
        custom_game = 1

    if(custom_game != 0):
        while True:
            gameLength = int(input("How many moves to perform?: "))
            if(gameLength > 0):
                break;
            else:
                print("You can't perform negative moves")

        while True:
            encounter_chance = int(input("What is a chance to encounter a chest? (in %): "))
            if(encounter_chance >= 0 & encounter_chance <= 100):
                break;
            else:
                print("Chance to encounter treasure must value from 0 to 100")

        green = int(input("Insert reward for green chest: "))
        yellow = int(input("Insert reward for yellow chest: "))
        violet = int(input("Insert reward for violet chest: "))
        golden = int(input("Insert reward for golden chest: "))

        while (gameLength > 0):
            if(is_Encounter(encounter_chance)):   #if encounter is true
                hoarded_gold += mixed_Rewards(reward_from_Chest(chests, green, yellow, violet, golden))
            else:
                print("You have found nothing. Better luck next time :(")
            gameLength -= 1
    else:   #standard game
        while (gameLength > 0):
            if(is_Encounter()):   #if encounter is true
                hoarded_gold += reward_from_Chest(chests)
            else:
                print("You have found nothing. Better luck next time :(")
            gameLength -= 1

    print("Game's over. Your accumulated wealth: ", hoarded_gold)

    #------------------------------------------------------------------------------------------
    from enum import Enum

    hoarded_gold = 0
    gameLength = 5
    Event = Enum('Event', ['Chest', 'Empty']) #enumerator

    #slownik zdarzen
    eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }

    eventList = tuple(eventDictionary.keys())
    eventProbability = tuple(eventDictionary.values())      #extracting probability
    print(eventDictionary,"\n",eventList,"\n",eventProbability)

    Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomaranczowy',
                           'Purple': 'fiolet',
                           'Gold': 'zloty'
                          }
               )

    chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }

    chestColourList = tuple(chestColoursDictionary.keys())
    chestColourProbability = tuple(chestColoursDictionary.values())
    print(chestColoursDictionary,"\n",chestColourList,"\n",chestColourProbability)

    rewardsForChests = {
                       chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                       for reward in range(len(chestColourList))
                   }

    while gameLength > 0:
        gamerAnswer = input("Do you want to move forward?")
        if (gamerAnswer == "yes"):
            print("Great, let's see what you got...")
            drawnEvent = random.choices(eventList,eventProbability)[0]
            if (drawnEvent == Event.Chest):
                print("You've drawn a CHEST")
                drawnColour = random.choices(chestColourList,chestColourProbability)[0]
                print("The chest color is", drawnColour.value)
                gamerReward = rewardsForChests[drawnColour]
                hoarded_gold = hoarded_gold + gamerReward
            elif(drawnEvent == Event.Empty):
                print("You've drawn nothing, you are so unlucky!")        
        else:
            print("You can go just straight man, nothing else, this game is dumb")
            continue   
        gameLength = gameLength - 1

    print("Congratulation, you have acquired: ", hoarded_gold)