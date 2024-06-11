import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.ejves.com/current"

# Perform a GET request to fetch the HTML content of the page
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the article titles on the page
# Note: The actual structure of the website may require specific tags or classes to be targeted
article_titles = soup.find_all('h3', class_='toc__item__title')  # Assuming 'h2' tag with class 'title' contains the article titles

# Extract and print the article titles
article_names = [title.text.strip() for title in article_titles]

# Output the article names
for name in article_names:
    print(name)
