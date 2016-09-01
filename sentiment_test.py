from bs4 import BeautifulSoup
import requests
import json 
from tokens import OcpKey 

url = 'https://en.wikipedia.org/wiki/Monty_Python'
payload = {
    'q': 'Python',
}
r = requests.get(url % payload)

soup = BeautifulSoup(r.text, "html.parser")
l = soup.find_all('p')
print l[0].text

words = l[0].text

data = {
    "documents": [
    {
      "language": "en",
      "id": "string",
      "text": words
    }
  ]
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': OcpKey}

r = requests.post(
    'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment',
    data=json.dumps(data),
    headers=headers 
    )

print r.text 