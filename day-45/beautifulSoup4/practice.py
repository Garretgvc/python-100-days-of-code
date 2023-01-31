from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

anchor_tags = soup.find_all(name="a")
for tag in anchor_tags:
    print(tag.getText)
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

soup.select(".headings")

