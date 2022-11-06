import requests
url_ddg = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'

resp_data = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

json_data = resp_data.json()['RelatedTopics']
