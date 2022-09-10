bidders = {}
name = ""
bid = 0
auctionInProgress = True
decision = ""
print("Welcome to the secret auction")

def highestBid(listOfBidders):
    highest = 0
    name = ""
    for key in listOfBidders:
        if(listOfBidders[key] > highest):
            highest = listOfBidders[key]
            name = key
    return {name: highest}


while auctionInProgress:
    name = input("Please enter your name: ")
    bid = float(input("Please enter your bid: "))
    decision = input("Is any other player around? yes or no").lower()
    bidders[name] = bid
    if(decision == "yes"):
        print("Please move away.")
    else:
        auctionInProgress = False
winner = highestBid(bidders)
print(winner)