import pandas

FILE_PATH = "./nato_phonetic_alphabet.csv"

nato_alphabet_data = pandas.read_csv(FILE_PATH)
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_alphabet_data.iterrows()}

while True:
    try:
        message = input("Please enter a message to code: ").upper().split()
        for word in message:
            str_word = str(word)
            coded_word = [nato_dict[char] for char in str_word]
            print("Message:", word, "-read as-", coded_word, sep = "   ")
    except KeyError:
        print("Only numbers and letter are allowed.")
    
