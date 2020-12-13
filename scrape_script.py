#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup
from retry import retry


URL = 'https://www.newsnow.co.uk/h/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'


@retry(Exception, tries=3, delay=5, backoff=2)
def get_response():
    session = requests.Session()
    response = session.get(URL, headers={
            'User-Agent': USER_AGENT
            })
    return response

def main():
    try:
        response = get_response()
    except Exception:
        sys.exit(1)   
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all("a", class_="hll")
    titles = [link.text for link in links]
    file = open ('output.txt', 'w') 
    file.write('\n'.join(titles)) 
    file.close ()


if __name__ == '__main__':
    main()
