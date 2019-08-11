import quote_scraper
from random import choice

quotes_info = quote_scraper.get_all_quotes()
game_over = False


def check_guess(answer, correct_answer):
    if answer == correct_answer:
        print("------------------------")
        print("Congratulations!")
        print("------------------------")
        return True
    return False


def play_again():
    user_input = input("Do you want to play again: Y/N")
    if user_input.lower() == "y" or user_input.lower() == "yes":
        return True
    return False


while not game_over:
    author, bio, quote = choice(quotes_info)
    print("\nGuess who wrote this quote:")
    print(quote)
    hints_used = 0
    while True:
        guess = input("Your guess: ")
        if not check_guess(guess, author):
            print("Incorrect! Try again!\n")
            if hints_used == 0:
                first_hint = quote_scraper.get_first_hint(bio)
                print(f"HINT: {first_hint}")
            elif hints_used == 1:
                print(f"HINT: First letter of the author is {author[0]}")
            elif hints_used == 2:
                print(f"HINT: First name of the author is {author.split(' ')[0]}")
            else:
                print(f"No hints left...Sorry!")
                print(f"The author was {author}!")
                game_over = True
                break
            hints_used += 1
        else:
            break
    if not play_again():
        print("\nThanks! Play again soon!\n")
        break
    else:
        game_over = False
        print("\n------------------------\n")


