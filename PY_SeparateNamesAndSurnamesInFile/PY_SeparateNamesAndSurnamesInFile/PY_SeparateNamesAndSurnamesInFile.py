def open_file(file_name):
    try:
        with open(file_name, 'r', encoding = 'UTF-8') as opened_file:
            return opened_file.read()
    except FileNotFoundError:
        print("File does not exist")
        return 0


if __name__ == '__main__':
    list_of_people = []
    with open("imionanazwiska.txt", "r", encoding = 'UTF-8') as main_file:      #automaticly closes the file
        for line in main_file:
            #changes the read line into the tuple and removes sign for the next line
            list_of_people.append(tuple(line.replace("\n", "").split(" ")))     
        with open("names.txt", "w", encoding = 'UTF-8') as file_names:
            #read list from the behing to the end
            for index in range(len(list_of_people)):
                #reads first element of the tuple located in index position and inserts it into the file
                file_names.write(list_of_people[index][0] + "\n") 
        with open("surnames.txt", "w", encoding = 'UTF-8') as file_surnames:
            #reads second element of the tuple located in index position and inserts it into the file
            for index in range(len(list_of_people)):
                #when surname is not found writes it into the file
                try:
                    file_surnames.write(list_of_people[index][1] + "\n")
                except IndexError:
                    file_surnames.write("- no surname found -\n")
    print(list_of_people)
    file_name = input("Podaj nazwe pliku jaki chcesz wczytac: ")
    mylist = open_file(file_name)
    print(mylist)