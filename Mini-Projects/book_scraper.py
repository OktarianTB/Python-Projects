import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books():
    response = requests.get("http://books.toscrape.com/catalogue/category/books/classics_6/index.html")
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")

    books_list = []
    for book in books:
        books_list.append((get_title(book), get_price(book), get_rating(book)))
    save_books(books_list)


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.find(class_="price_color").get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.find(class_="star-rating")
    rating_text = paragraph.get_attribute_list("class")[-1]
    return ratings[rating_text]


def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute("CREATE TABLE books (title TEXT, price REAL, rating INTEGER)")
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()


scrape_books()
