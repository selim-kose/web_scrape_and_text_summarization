from bs4 import BeautifulSoup
import requests

def get_text(url):
    response = requests.get(url)
    website_content = BeautifulSoup(response.content)
    print(website_content)
    text = ' '.join([p.text for p in website_content.find_all('p')])
    print("""
    -------------------------
    -------------------------
    """)
    print(text)
    return text

get_text("https://en.wikinews.org/wiki/Global_markets_plunge")
