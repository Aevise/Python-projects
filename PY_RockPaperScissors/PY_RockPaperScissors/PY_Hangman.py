from random import randint

words_list = ["Ziolo", "Bagietka", "Naserka", "Cyprian", "Dzieciatko"]
words_list_length = len(words_list) - 1
word = words_list[randint(0, words_list_length)]
player_list = []

for letter in word:
    player_list.append(letter)

print(player_list)
check = ""
check = check.join(player_list)
print(check)