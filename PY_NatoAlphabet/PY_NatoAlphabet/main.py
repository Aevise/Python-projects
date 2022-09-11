import pandas

FILE_PATH = "./nato_phonetic_alphabet.csv"

nato_alphabet_data = pandas.read_csv(FILE_PATH)
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_alphabet_data.iterrows()}

while True:
    try:
        word = input("Please enter a word to code: ").upper().replace(" ", "")
        coded_word = [nato_dict[letter] for letter in word]
        print(coded_word)
    except KeyError:
        pass
    
