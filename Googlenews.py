import requests
from bs4 import BeautifulSoup

# URL for the Google News search query
url = 'https://news.google.com/search?q=law&hl=en-IN&gl=IN&ceid=IN%3Aen'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all article elements
articles = soup.find_all('article')

# List to store the news articles
newslist = []

# Set the limit for the number of articles
limit = 10
count = 0

for item in articles:
    if count >= limit:
        break
    try:
        # Find the title element using the class 'JtKRv'
        title_elem = item.find(class_='JtKRv')
        # Find the link element
        link_elem = item.find('a', href=True)
        
        if title_elem and link_elem:
            newsarticle = {
                'title': title_elem.get_text(),
                'link': 'https://news.google.com' + link_elem['href'][1:]  # Removing the leading dot
            }
            newslist.append(newsarticle)
            count += 1
    except Exception as e:
        print(f"Error: {e}")

# Print the news articles in proper format
for article in newslist:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}\n")
