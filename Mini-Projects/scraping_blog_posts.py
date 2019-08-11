import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        title = article.find("a").get_text()
        link = article.find("a")["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, link, date])
