import requests
url = "https://quotes.toscrape.com/"
resp = requests.get(url)

print(resp.headers['Content-Type'])

