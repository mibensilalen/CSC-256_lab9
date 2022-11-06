import requests
url= 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'

resp_data = requests.get(url + "/?q=DuckDuckGo&format=json")

json_data = resp_data.json()['RelatedTopics']
