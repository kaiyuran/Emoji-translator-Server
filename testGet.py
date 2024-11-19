import requests

url = "http://127.0.0.1:5000/getemoji"

params = {
    "message": "I love chocolate donuts. I laugh at funny jokes about it. I think it is amazing."
}

r = requests.get(url, params=params)

data = r.json()
print(list(data.keys()))
finalMessage = data["message"]
print(finalMessage)