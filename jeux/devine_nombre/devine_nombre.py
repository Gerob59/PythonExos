import random


def get_guess_from_user(guess_num: int):
    guess = input(f"Essai no {guess_num}\nVotre proposition : ")
    try:
        return int(guess)
    except ValueError:
        print("Entrez un nombre entier.")
        return None


def print_guess_result(guess: int, to_find: int, guess_num: int):
    if guess == to_find:
        print(f"Bravo ! Vous avez trouvé {to_find} en {guess_num} essais !")
    elif guess < to_find:
        print("Trop petit")
    else:
        print("Trop grand")


def play_guessing_game():
    to_find: int = random.randint(1, 30)
    max_guesses: int = 5

    print(f"J'ai choisi un nombre entre 1 et 30.\nA vous de le deviner en {max_guesses} tentatives au maximum !")

    for guess_num in range(1, max_guesses + 1):
        guess = get_guess_from_user(guess_num)
        if guess is None:
            continue
        print_guess_result(guess, to_find, guess_num)
        if guess == to_find:
            return

    print(f"Perdu. Le nombre que vous cherchez était {to_find} !")


if __name__ == '__main__':
    play_guessing_game()
