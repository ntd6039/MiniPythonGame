import random
#defines class Trainer who will then be the user's class and class pomeon who will be the input class and have the elemental type chart within th class.
class Trainer:
    def __init__(self, name):
        self.name = name
        self.wins = 0
    
    def win(self):
        self.wins += 1
        
class Pokemon:
    def __init__(self, type):
        self.type = type
        self.wins_against = []

    def set_wins_against(self, types):
        self.wins_against = types

    def check_win(self, opponent_type):
        return opponent_type in self.wins_against


types = {
    'fire': ['grass', 'ice'],
    'water': ['fire', 'ground'],
    'grass': ['ground'],
    'ground': ['fire'],
    'ice': ['grass', 'ground']
}
#Pokemon class inheriting elemental weaknesses
pokemons = {}
for key in types:
    pokemons[key] = Pokemon(key)
    pokemons[key].set_wins_against(types[key])

# get the user's name
user_name = input("What is your name? ")
user_trainer = Trainer(user_name)

# get the rival's name
rival_name = input("What is your rival's name? ")
rival_trainer = Trainer(rival_name)

# repeat battle 6 times
for i in range(6):
    # get user type for each round
    user_type = input(f"Round {i+1}: What type do you choose? (fire, water, grass, ground, ice) ").lower()
    rival_type = random.choice(list(types.keys()))
    print(f"{user_name} chose a {user_type} Pokemon")
    print(f"{rival_name} chose a {rival_type} Pokemon")

    # check if user wins
    if pokemons[user_type].check_win(rival_type):
        user_trainer.win()
        print(f"{user_name} wins this round!")
    # check if rival wins
    elif pokemons[rival_type].check_win(user_type):
        rival_trainer.win()
        print(f"{rival_name} wins this round!")
    # if it's a tie
    else:
        print("It's a tie!")
    print()

# check who wins the overall battle
if user_trainer.wins > rival_trainer.wins:
    print(f"{user_name} wins the battle and becomes the champion!")
elif user_trainer.wins < rival_trainer.wins:
    print(f"{rival_name} wins the battle. {user_name} lost but should never give up!")
else:
    print("It was a formidable battle indeed, it is a tie!")