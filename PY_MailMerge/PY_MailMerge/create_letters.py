MY_NAME = "Meteo"
PATH_TO_NAMES = "../Input/Names/invited_names.txt"
PATH_TO_LETTER = "../Input/Letters/starting_letter.txt"
PATH_WHERE_GENERATE = "../Output/ReadyToSend/"
TO_CHANGE = ["[name]", "[signature]"]

def create_name_list()->list:
    """Reads names from a file. Each line has to contain only name
    Returns:
        list: each index is a different name
    """
    #can also use readlines() method
    new_list = []
    with open(file = PATH_TO_NAMES, mode = "r") as file:
        for name in file:
            new_list.append(name.strip("\n"))
    return new_list

def create_letters(names_list:list)->None:
    """Generates a letter based on a template.
    Args: names_list -> reads names from the list and puts a name in the template
    """
    with open(file = PATH_TO_LETTER, mode = "r") as file:
        basic_content = file.read()
    for name in names_list:
        file_name = PATH_WHERE_GENERATE + f"/Letter for {name}.txt"
        with open(file = file_name, mode = "w") as file:
            text = basic_content.replace(TO_CHANGE[0], name)
            text = text.replace(TO_CHANGE[1], MY_NAME)
            file.write(text)
