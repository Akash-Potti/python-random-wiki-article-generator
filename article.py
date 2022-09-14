from cgitb import text
from turtle import title
import requests
from bs4 import BeautifulSoup
import webbrowser
print("Press ENTER")
while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title}\n Do you want to read the article? (yes/no)")
    ans = input("").lower()

    if ans == "yes":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == 'no':
        print("Try Again!!")
        continue
    else:
        print("Wrong command! .Try again")
        break
