from bs4 import BeautifulSoup
import requests


# WARNING: this script could stop working since the website can change its structure.
# In fact this version is different from the course.

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.prettify())

# Get all the links
articles = soup.select(selector="span.titleline > a")  # We want to select the first descending "a" tag.

print(articles)
print(f"Number of articles: {len(articles)}")

for article in articles:
    print("###############################################")
    print(article.getText())
    print(article.get("href"))
    print("###############################################")
    # We can't get upvotes because the website has changed its structure.

