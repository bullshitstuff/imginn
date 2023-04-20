import requests
from bs4 import BeautifulSoup
import json

def getPostContents(url):
    # Send a GET request to the URL and get the HTML content
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
    }
    
    response = requests.get(url, headers=headers)
    html = response.content
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract the URL of the image associated with the post
    try:
        content_url = soup.find('div', {'class': 'media-wrap'})['src']
        description = soup.find('meta', {'name': 'description'})['content']
    except KeyError:
        # Extract the contents of the JSON-LD script
        json_ld = soup.find('script', {'type': 'application/ld+json'}).text
            
        # Parse the JSON and extract the contentUrl key value
        data = json.loads(json_ld)
        content_url = data['contentUrl']
        description = data['description']
        # Return the image URL and content URL
    return content_url, description
    
print(getPostContents("https://imginn.org/p/CqcbR53odup/"))
