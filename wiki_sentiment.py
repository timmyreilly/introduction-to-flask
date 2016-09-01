from bs4 import BeautifulSoup
import requests
import json 
from tokens import * 

def get_sentiment_from_url(url='https://en.wikipedia.org/wiki/Monty_Python'):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    l = soup.find_all('p')
    h = soup.find_all('h1')
    #print l[0].text

    words = l[0].text
    data = {"documents": [{"language": "en","id": "string","text": words}]}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': OcpKey}
    url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    r = requests.post(url, data=json.dumps(data), headers=headers)

    content = json.loads(r.content)
    return content['documents'][0]['score'], str(h[0].text) 








