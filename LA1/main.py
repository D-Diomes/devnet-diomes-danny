import requests
import random

def main ():
    player = 1
    while player <= 3:
        number = random.randrange(1, 5)
        print(f"The number is : {number}")
        if number == 1:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/1')
            pokemon = pokedex.json()
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 2:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/2')
            pokemon = pokedex.json()
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 3:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/3')
            pokemon = pokedex.json()
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 4:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/4')
            pokemon = pokedex.json()
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 5:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/5')
            pokemon = pokedex.json()
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        else:
            print("The pokemon is: ")
        
        print(guess = input("Who is the Pokemon [bulbasaur, ivysaur, venusaur, charmander, charmeleon]: "))

main()