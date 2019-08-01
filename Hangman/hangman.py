import random

file_name = "words.txt"


def get_random_word():
    try:
        with open(file_name, "r") as words_text:
            words = words_text.readlines()
            if len(words) > 2:
                index = random.randint(0, len(words) - 1)
                return words[index].replace("\n", "")
            return None
    except FileNotFoundError:
        return None


def display_hidden_word(letters, word):
    hidden_word = ""
    word_completed = True

    for char in word:
        if char == word[0]:
            hidden_word += word[0] + " "
        elif char in letters:
            hidden_word += char + " "
        else:
            hidden_word += "_ "
            word_completed = False

    return hidden_word, word_completed


def print_tries_left(tries_left):
    if tries_left > 1:
        print(f"You have {tries_left} tries left.")
    else:
        print(f"You have {tries_left} try left.")


def play_game():
    word_to_guess = get_random_word()

    if word_to_guess is None:
        print("Error!")
        return

    letters_tried = [word_to_guess[0]]
    tries_left = 10

    while True:
        hidden_word = display_hidden_word(letters_tried, word_to_guess)

        print("\n-------------------------\n")

        if hidden_word[1] is True:
            print(f"Finished! The word was '{word_to_guess}'")
            break

        print(f"The word you are trying to find is: {hidden_word[0]}")
        print(f"You have tried the following letters: {letters_tried}")
        print_tries_left(tries_left)
        player_input = input("Enter a letter: ")

        if len(player_input) == 1 and player_input.isalpha():
            if player_input in letters_tried:
                print("You have already tried this letter!")
                continue
            letters_tried.append(player_input)
            if player_input not in word_to_guess:
                tries_left -= 1
        else:
            print("\n-------------------------\n")
            print("Incorrect input! Try again!")
            continue

        if tries_left <= 0:
            print("\n-------------------------\n")
            print(f"Game Over! No more tries left. The word was: '{word_to_guess}'")
            break


play_game()
