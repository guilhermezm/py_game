import time
import random
RED = "\033[31m"
RESET = "\033[0m"

def choose_action(actions):
    # Convert dictionary keys to a list and shuffle
    keys = list(actions.keys())
    random.shuffle(keys)
    choices = keys[:3]  # Select three choices randomly

    # Display the choices to the user (only keys)
    print("Choose one of the following actions:")
    for idx, key in enumerate(choices, 1):
        print(f"{idx}. {key}")

    # Get user input and validate it
    while True:
        try:
            user_input = int(input("Enter your choice (1, 2, or 3): "))
            if 1 <= user_input <= 3:
                chosen_key = choices[user_input - 1]
                # Display the corresponding message after the choice
                print(f"You chose to: {chosen_key}")
                print(f"{actions[chosen_key]}")  # Display the message associated with the key
                return chosen_key  # Return the key of the chosen action
            else:
                print("Invalid input, please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

def damage(life, damage):
    life -= damage
    print(f"You missed it! -{damage}. life: {life}")
    if life < 0:
        raise Exception('You died')
    else:
        return life

def villons_challange(i, fases, enemies, life):
    i_villon = 1
    random.shuffle(fases[i]["enemies"])
    for villon_key in fases[i]["enemies"]:
        while True:
            start_time = time.time()
            kill_input = input(f"Type {RED}{enemies[villon_key]['sequence']}{RESET} in less than {enemies[villon_key]['time']} sec")
            if kill_input == enemies[villon_key]['sequence'] and (time.time() - start_time) <= enemies[villon_key]['time']:
                print(f"Congratulations! You shot {villon_key} n{i_villon}")
                i_villon += 1
                break
            else:
                life = damage(life, enemies[villon_key]['damage'])
    return life
