# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
import random

movies_list = ["armageddon", "lord of the rings", "up", "rush hour", "zorro", "the mask", "once upon a time", "the expendables"]
williams_movies_won = ["Jaws", "Star Wars: Episode IV - A New Hope ", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]
some_toto_albums = ["Toto", "Hydra", "Turn Back", "Toto IV", "Isolation", "Fahrenheit", "The seventh one", "Kinfdom od Desire",
                    "Tambu", "Mindfields", "Old Is New", "Through the looking glass"]

def alphabetical_order(a):
    a.sort()
    return a

print(alphabetical_order(movies_list))

def won_golden_globe(movie):
    check = movie in [x.lower() for x in williams_movies_won] or movie in [x.upper() for x in williams_movies_won]
    return check

print(won_golden_globe("jaws"))
print(won_golden_globe("Dune"))

def oops(a):
    random_album = (random.choice(a))
    movies_list.append(random_album)
    return movies_list

print(oops(some_toto_albums))
print(alphabetical_order(movies_list))

def remove_toto_albums(original_list):
    original_list = [i for i in movies_list if i not in some_toto_albums]
    return original_list

print(remove_toto_albums("Old Is New"))