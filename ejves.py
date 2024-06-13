import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.clinicalkey.com/#!/browse/toc/1-s2.0-S1078588424X00052/null/journalIssue"

# Adding headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Sending a request to fetch the content of the webpage
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check if the request was successful

# Parsing the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all article elements within <h3> tags
articles = soup.find_all('h3')

# Extracting the article titles and links
article_list = []
for article in articles:
    a_tag = article.find('a')
    if a_tag:
        title = a_tag.get_text(strip=True)
        link = a_tag['href']
        article_list.append({'title': title, 'link': link})

# Print the articles
for article in article_list:
    print(f"Title: {article['title']}\nLink: {article['link']}\n")
