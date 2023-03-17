""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

from helpers import get_countries
import string

def shortest_names():
    shortest_length = len(min(countries, key=len))
    shortest_countries_list = []
    for country in countries:
        if shortest_length == len(country):
            shortest_countries_list.append(country)
    return shortest_countries_list

def most_vowels(countries):
    vowels = ["a","e","i","o","u"]
    vowels_count = {}
    for country in countries:
        count = 0
        for character in country:
            if character.lower() in vowels:
                count +=1
        vowels_count[country] = count
        sorted_vowels = sorted(vowels_count.items(), key=lambda vowel: vowel[1], reverse=True)
    return [sorted_vowels[vowel_most][0] for vowel_most in range(3)]

def alphabet_set(countries):
    alphabet = set(string.ascii_lowercase)
    countries_added = []
    for country in sorted(countries, key=lambda vowel: len(set(vowel.lower()) - alphabet)):
        letter_set = set(country.lower())
        for letter in letter_set:
            if letter in alphabet:
                countries_added.append(country)
                alphabet -= letter_set
        if alphabet == set():
            break
    return countries_added

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()


print(alphabet_set(countries))