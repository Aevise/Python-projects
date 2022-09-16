from random import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(min_letters: int = 8, max_letters: int = 10, min_symbols: int = 2, max_symbols: int = 4, min_numbers: int = 2, max_numbers: int = 4)->str:
    """Generates random password.

    Args:
        min_letters (int, optional): minimum number of letters in the password. Defaults to 8.
        max_letters (int, optional): maximum number of letters in the password. Defaults to 10.
        min_symbols (int, optional): minimum number of symbols in the password. Defaults to 2.
        max_symbols (int, optional): maximum number of symbols in the password. Defaults to 4.
        min_numbers (int, optional): minimum number of numbers in the password. Defaults to 2.
        max_numbers (int, optional): maximum number of numbers in the password. Defaults to 4.

    Returns:
        str: password created from random chars.
    """ 
    letters_list = [choice(letters) for _ in range(randint(min_letters, max_letters))]
    symbols_list = [choice(symbols) for _ in range(randint(min_symbols, max_symbols))]
    numbers_list = [choice(numbers) for _ in range(randint(min_numbers, max_numbers))]
    password = letters_list + symbols_list + numbers_list
    shuffle(password)
    password = "".join(password)
    return password





