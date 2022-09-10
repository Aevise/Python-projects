import requests
import json
import pprint
import webbrowser
import credentials

def Verify_Facts():
    stubborn_Maupos = 1
    while stubborn_Maupos:
        verify_facts = input("Should Malpos verify theses facts? Please write yes or no: ")
        if(verify_facts.capitalize() == "Yes"):
            return True
        elif(verify_facts.capitalize() == "No"):
            return None
        else:
            print("Panios is too smart for that")

def list_of_collected_cat_facts(how_much_facts, animal_type = "cat"):
    collected_cat_facts = []
    catfacts_params = {
        "animal_type": animal_type,            
        "amount": how_much_facts,
                    }
    catfacts_website = requests.get("https://cat-fact.herokuapp.com/facts/random/", params = catfacts_params)
    try:
        catfacts = catfacts_website.json()
    except json.decoder.JSONDecodeError:
        print("Maupos Fucked up")
    else:
        verified = Verify_Facts()
        for cat_fact in catfacts:
            if(cat_fact["status"]["verified"] == verified):
                collected_cat_facts.append(cat_fact["text"])
    return collected_cat_facts
#-----------------------------------------------------------------------------------------------
#---------------------api_key przeslany jawnie ---------------------------------------------------
def available_cat_breeds():
    cat_photos_website = requests.get("https://api.thecatapi.com/v1/breeds")
    number = 1
    dictionary_of_cat_breeds = dict()
    try:
        cat_breeds = cat_photos_website.json()
    except json.decoder.JSONDecodeError:
        print("Maupos Fucked up")
    else:
        print("Panios please choose from one of these breeds")
        for cat_breed in cat_breeds:
            print(number,"->", cat_breed["name"])
            dictionary_of_cat_breeds[cat_breed["name"]] = cat_breed["id"]
            number += 1
        return dictionary_of_cat_breeds

def choose_breed(dictionary_of_breeds):
    selected_breed = ""
    while True:
        selected_breed = input("Please type in the name of breed: ")
        if(selected_breed.title() in dictionary_of_breeds.keys()):
            return dictionary_of_breeds[selected_breed.title()]

def list_of_links_to_cat_photos(cat_breed, how_much):
    links_to_photos = []
    cat_photos_params = {
        "breed_ids": cat_breed,            
        "limit": how_much,
        "api_key": "2d2c9093-220b-4ed1-8c13-b92b5ceb39d3"
                    }
    cat_photos_website = requests.get("https://api.thecatapi.com/v1/images/search", params = cat_photos_params)
    try:
        cat_photos = cat_photos_website.json()
    except json.decoder.JSONDecodeError:
        print("Maupos Fucked up")
    else:
        for cat_photo in cat_photos:
            links_to_photos.append(cat_photo["url"])
        return links_to_photos
#-----------------------------------------------------------------------------------------------
#-------------------------autoryzacja przez header -----------------------------------------
def amount_check(default_max = 10):
    print("Current maximum amount is:", default_max)
    while True:
        try: 
            how_many = int(input("How many cat photos do Panios require?: "))
            if(how_many <= default_max):
                return how_many
            else:
                print("Panios too smart for that")
        except ValueError:
            print("Panios is too smart for that")

def link_opener(list_with_links):
    for link in list_with_links:
        webbrowser.open_new_tab(link)

def get_json_from_website(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Maupos Fucked up")
    else:
        return content
#-----------------------------------------------------------------------------------------------

def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", headers = credentials.header)
    return get_json_from_website(r)

def add_favourite_cat(cat_ID, userId): #wysylanie danych o dodaniu kotka do ulubionych na serwer
    cat_Data = {"image_id": cat_ID,
              "sub_id":userId
            }
    r = requests.post("https://api.thecatapi.com/v1/favourites", json = cat_Data, headers = credentials.header)
    return get_json_from_website(r)

def get_favourite_cats(userID):
    params = {
            "sub_id":userID
            }
    r = requests.get("https://api.thecatapi.com/v1/favourites", params, headers = credentials.header)
    return get_json_from_website(r)

def remove_favourite_cat(userID, favourite_catID):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/" + favourite_catID, headers = credentials.header)
    return get_json_from_website(r)

if __name__ == '__main__':

#-----------------------------------------------------------------------------------------------    
#    too_much_knowledge = 1
#    while too_much_knowledge:
#        try:
#            how_many_cat_facts = int(input("Panios, please tell me how many cat facts should Maupos read? \nMaupos, 'read': "))
#            if(how_many_cat_facts > 500):
#                print("Panios want to know too much but Maupos cannot aquire so much knowledge. Please try again")
#            else:
#                too_much_knowledge = 0
#        except ValueError:
#            print("Panios is too smart for that")
#    cat_facts = list_of_collected_cat_facts (how_many_cat_facts)
#    for facts in cat_facts:
#        print(facts)
#-----------------------------------------------------------------------------------------------    
    dictionary_of_cat_breeds = available_cat_breeds()
    chosen_breed = choose_breed(dictionary_of_cat_breeds)
    how_many = amount_check()
    cat_photos_links = list_of_links_to_cat_photos(chosen_breed, how_many)
    automatic_opening_of_links = input("Should I open links automaticly? Type yes otherwise Maupos won't do it.\n")
    if (automatic_opening_of_links.capitalize() == "Yes"):
        link_opener(cat_photos_links)
    else:
        print("Found links:")
        for items in cat_photos_links:
            print(items)
#-----------------------------------------------------------------------------------------------    
    #ustawianie headera;
    #przesylamy go do argumentu nazwanego header zamiast wpisywac go do params
    userID = "hdf2"
    random_cat = get_random_cat()
    print("Random Cat:", random_cat[0]["url"])
    while True:
        add_Favourite = input("Do you want to save this photo as your favourite?: Yes/No\n")
        add_Favourite.capitalize()
        if (add_Favourite == "Yes"):
            print("A wise choice!")
            break
        elif(add_Favourite.capitalize() == "No"):
            print("What a shame")
            break
        else:
            print("Try again")
    favourite_cats = get_favourite_cats(userID)
    dictionary_of_cats = { 
                           cat["id"] : cat["image"]["url"] #dla kazdego kota w favourite_cats stworz klucz w slowniku o nazwie cay[id] a nastepnie przypisz do tego klucza link do rzeczonego kotka
                           for cat in favourite_cats
                          }
    print("Your favourite cats are: ", dictionary_of_cats)

    while True:
        heartless = input("Are you sure that you want to remove a cat?: yes/no\n")
        if (heartless.capitalize() == "Yes"):
            print("Bastard")
            cat_id_to_delete = input("Type in cat ID: ")
            print(remove_favourite_cat(userID, cat_id_to_delete))
            break
        elif (heartless.capitalize() == "No"):
            print("It's your lucky day")
            break
        else:
            print("Wut?")

    print("Your favourite cats are: ", dictionary_of_cats)