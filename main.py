import requests

res = requests.get("https://ya.ru")
print(res.content)