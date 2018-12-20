# Web scraper that pulls frontpage articles from CoinDesk.com (cryptocurrency site) and saves them to a CSV file.

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.coindesk.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open("coindesk_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Date','Summary', 'URL'])

for article in soup.find_all('a', class_="stream-article"):

    title = article.find('div', class_="meta").h3.text
    print(title)

    article_date = article.find('div', class_="time").text
    print(article_date)

    summary = article.find('p').text
    print(summary)
    
    web_link = article.get('href')
    print(web_link)

    print()

    csv_writer.writerow([title, article_date, summary, web_link])

csv_file.close()


