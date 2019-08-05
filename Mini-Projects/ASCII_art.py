import pyfiglet
import termcolor

text = input("Enter the text you want converted: ")
color = input("Enter your desired color: ").lower()


try:
    ascii_text = pyfiglet.figlet_format(text)
    colored_text = termcolor.colored(ascii_text, color)
    print(colored_text)
except KeyError:
    print("Incorrect input!")