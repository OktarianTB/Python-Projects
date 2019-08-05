with open("pi.txt", "r") as pi:
    value = pi.read().replace("\n", "")

birthday = input("Enter your birthday: XX/XX/XX for DAY/MONTH/YEAR: ")
index = value.find(birthday.replace("/", ""))

if index != -1:
    print(f"Your birthday {birthday}, can be found from the {index-1}th digit of pi")
    try:
        numbers = [value[i] for i in range(index-5, index+10)]
        print(numbers)
    except IndexError:
        pass
else:
    print(f"Your birthday {birthday}, can't be found in the first 100,000 digits of pi. Sorry!")
