import requests
from bs4 import BeautifulSoup


def get_all_quotes():
    i = 1
    information = []
    while True:
        response = requests.get("http://quotes.toscrape.com/page/" + str(i))
        soup = BeautifulSoup(response.text, "html.parser")
        sections = soup.find_all(class_="quote")

        for section in sections:
            quote = section.find(class_="text").get_text()
            author = section.find(class_="author").get_text()
            bio = section.find("a")["href"]
            information.append([author, bio, quote])

        if soup.find(class_="next"):
            i += 1
        else:
            return information


def get_first_hint(link):
    response = requests.get("http://quotes.toscrape.com" + link)
    soup = BeautifulSoup(response.text, "html.parser")

    date = soup.find(class_="author-born-date").get_text()
    location = soup.find(class_="author-born-location").get_text()

    return f"Born: {date} {location}"