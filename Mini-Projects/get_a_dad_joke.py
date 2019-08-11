import requests

url = "https://icanhazdadjoke.com/search"

while True:
    term = input("\nEnter the theme of the joke: ")
    req = requests.get(url, headers={"Accept": "application/json"}, params={"term": term})
    data = req.json()
    jokes_available = len(data["results"])
    index = 0

    if jokes_available:
        print(f"There are {jokes_available} jokes available!")
        while index < jokes_available:
            print(data["results"][index]["joke"])
            index += 1
            if index == jokes_available:
                break
            if input("Press C to continue or another key to stop: ").lower() != "c":
                break
    else:
        print("No jokes available for that theme")

