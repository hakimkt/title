import sys
import requests
from bs4 import BeautifulSoup

def get_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        if title:
            return title.text.strip()
    except Exception:
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls_file = sys.argv[1]
        with open(urls_file) as f:
            urls = f.read().splitlines()
    else:
        urls = sys.stdin.read().splitlines()

    for url in urls:
         title = get_title(url)
         if title:
             print(f'{url}\t{title}')
