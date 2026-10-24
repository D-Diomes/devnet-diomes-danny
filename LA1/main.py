import requests
import random

def main ():
    number = random.randrange(1, 6)
    # print(f"The number is : {number}")
    try: 
        if number == 1:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/1', timeout=10)
            if pokedex.status_code != 200:
                print(f"Failed (Status code: {pokedex.status_code})")
                return
            pokemon = pokedex.json()
            name = pokemon["name"]
            ability = pokemon["abilities"][0]["ability"]["name"]
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Ability of this pokemon is : {ability}")
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 2:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/2', timeout=10)
            if pokedex.status_code != 200:
                print(f"Failed (Status code: {pokedex.status_code})")
                return
            pokemon = pokedex.json()
            name = pokemon["name"]
            ability = pokemon["abilities"][0]["ability"]["name"]
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Ability of this pokemon is : {ability}")
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 3:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/3', timeout=10)
            if pokedex.status_code != 200:
                print(f"Failed (Status code: {pokedex.status_code})")
                return
            pokemon = pokedex.json()
            name = pokemon["name"]
            ability = pokemon["abilities"][0]["ability"]["name"]
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Ability of this pokemon is : {ability}")
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 4:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/4', timeout=10)
            if pokedex.status_code != 200:
                print(f"Failed (Status code: {pokedex.status_code})")
                return
            pokemon = pokedex.json()
            name = pokemon["name"]
            ability = pokemon["abilities"][0]["ability"]["name"]
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Ability of this pokemon is : {ability}")
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")
        elif number == 5:
            pokedex = requests.get('https://pokeapi.co/api/v2/pokemon/5', timeout=10)
            if pokedex.status_code != 200:
                print(f"Failed (Status code: {pokedex.status_code})")
                return
            pokemon = pokedex.json()
            name = pokemon["name"]
            ability = pokemon["abilities"][0]["ability"]["name"]
            height = pokemon["height"]
            weight = pokemon["weight"]
            print(f"The Ability of this pokemon is : {ability}")
            print(f"The Height of this pokemon is : {height}")
            print(f"The Weight of this pokemon is : {weight}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return

    player = 1
    while player <= 3:
        guess = input(f"Attempt {player}/3 - Who is the Pokemon [bulbasaur, ivysaur, venusaur, charmander, charmeleon]: ").strip().lower()

        valid_choices = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon"]
        if guess not in valid_choices:
            print("Invalid Pokémon name! Please choose from the provided list.")
            continue

        if guess == name:
            print("Correct guess!")
            return
        else:
            print("Incorrect guess!")

        player += 1

    print(f"Attempts ran out! The Pokémon was: {name}")

main()