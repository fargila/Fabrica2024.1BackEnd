import requests

manaira = request.get("API/CEP/")
json = manaira.json()

print(manaira)
print(json)