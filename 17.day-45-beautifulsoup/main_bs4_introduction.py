from bs4 import BeautifulSoup
import lxml

with open('./website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# Print the first <a> tag
print(soup.a)

# Print all <a> tags
all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

# Print all <a> tags' string
for tag in all_anchor_tags:
    print(tag.getText())

# Print all <a> tags' href
for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

# Nested tags
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

elements_by_class = soup.select(selector=".heading")
print(elements_by_class)
