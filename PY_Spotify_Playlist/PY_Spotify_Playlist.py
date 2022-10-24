from bs4 import BeautifulSoup
import requests
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler

WEBSITE = "https://www.billboard.com/charts/hot-100/"

def check_list_length(data:list, length:int = 3)->bool:
    """check if splitted data matches the length of data format

    Args:
        data (list): splitted data
        length (int, optional): length of data format. Defaults to 3.

    Returns:
        bool: matches the format or not
    """
    if len(data) != length:
        print("Wrong Format. Format: YYYY-MM-DD")   #raise ValueError("Wrong Format. Format: YYYY-MM-DD")
        return False
    else:
        return True

def check_data(data:list, year:int = 4, month_day:int = 2)->bool:
    """check if provided data matches the given format

    Args:
        data (list): data typed in by the user
        year (int, optional): amount of numbers in year. Defaults to 4.
        month_day (int, optional): amount of numbers in day or month. Defaults to 2.

    Returns:
        bool: True or False
    """
    length=[]
    curr_year = datetime.datetime.today().year
    for number in data:
        length.append(len(number))
    if length[0] != year:
        return False
    else:
        if int(data[0]) >= curr_year:
            if no_future_travel(data):
                for i in range(2):
                    if length[i+1] != month_day:
                        print("Wrong Format. Format: YYYY-MM-DD")
                        return False
                    elif i+1 == 1 and int(data[i+1]) > 12:
                        print("Wrong Format. Format: YYYY-MM-DD")
                        return False
                    elif i+1 == 2 and int(data[i+1]) > 31:
                        print("Wrong Format. Format: YYYY-MM-DD")
                        return False
            else:
                return False
        else:
            for i in range(2):
                if length[i+1] != month_day and i+1 == 1 and int(data[i+1]) > 12:
                    print("Wrong Format. Format: YYYY-MM-DD")
                    return False
                elif length[i+1] != month_day and i+1 == 2 and int(data[i+1]) > 12:
                    print("Wrong Format. Format: YYYY-MM-DD")
                    return False            
    return True

def no_future_travel(data:list)->bool:
    """Check whether we don't type a data in the future

    Args:
        data (list): format [yyyy, mm, dd]

    Returns:
        bool: True or False
    """
    todo = datetime.datetime.today().strftime('%Y-%m-%d')
    todo = todo.split("-")
    today = [int(element) for element in todo]
    increment = 0
    for element in data:
        if int(element) > today[increment]:
            return False
        increment += 1
    return True

def get_song_uris(auth:spotipy.Spotify, song_data:list)->list:
    """get a songs uri from spotify

    Args:
        auth (spotipy.Spotify): authentication data 
        song_data (list): list of tuples containing: (author, track name)

    Returns:
        list: list of sons uris. When song is not found, skips the song.
    """
    song_uris = []
    for song in song_data:
        try:
            data_received = auth.search(q=f"track:{song[1]} artist:{song[0]}", type="track")
            uri = data_received["tracks"]["items"][0]["uri"]
        except IndexError:
            pass
        else:
            song_uris.append(uri)
    return song_uris

def get_songs_data(song_list:BeautifulSoup)->list:
    """returns a list of tuples as: (author, song)
    return song_data
    """
    songs = song_list.find_all("h3", class_ = "a-no-trucate")
    authors = song_list.find_all("span", class_ = "a-no-trucate")
    song_data = [(author.getText().strip(), song.getText().strip()) for (author, song) in zip(authors, songs)]      #create a list of tuples as: (author, song)
    return song_data

def generate_playlist(auth:spotipy.Spotify, id_of_user:str, playlist_name:str, song_uris:list, is_public:bool = False)->None:
    """Generates playlist on spotify

    Args:
        auth (spotipy.Spotify): spotipy authentication token
        id_of_user (str): id of user
        playlist_name (str): name of a playlist
        song_uris (list): uri of songs got from spotify website
        is_public (bool, optional): should playlist be public. Defaults to False.
    """
    playlist = auth.user_playlist_create(user=id_of_user, name=playlist_name, public=is_public)
    auth.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print("Success!")

#-----------------------------------------------------------------------------------------------------------------
numbers = []
action = True

while action:
    no_error = True
    original_data = input("Type the date you want to get 100 songs. Format: YYYY-MM-DD\n")
    date = original_data.split("-")
    if check_list_length(date):
        for number in date:
            try:
                numbers.append(int(number))
            except ValueError:
                no_error = False
                print("Wrong Format. Format: YYYY-MM-DD")
                break
    if no_error:
        if check_data(date):
            action = False

web_address = WEBSITE + original_data
response = requests.get(web_address).text
soup_data  = BeautifulSoup(response, "html.parser")
songs_data = get_songs_data(soup_data)

spotify_cache_handler = CacheFileHandler("token.txt")

#FOR THE PROGRAM TO WORK PROVIDE YOUR OWN SPOTIFY CLIENT ID AND SPOTIFY SECRET
spotify_auth = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_handler=spotify_cache_handler
    )
)
user_id = spotify_auth.current_user()["id"]
uris = get_song_uris(spotify_auth, songs_data)
generate_playlist(spotify_auth, user_id, original_data, uris)