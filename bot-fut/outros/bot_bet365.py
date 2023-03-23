import requests
from pandas import json_normalize

# url = "https://api.aiscore.com/v1/web/api/matches"

# querystring = {"lang":"5","sport_id":"1","date":"20230321","tz":"-03:00"}

# payload = ""
# headers = {"cookie": "aiclient=kgm0ru4mpnw3108"}

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
# 'brasileirãosériea'

# import requests

# url = "https://football98.p.rapidapi.com/competitions"

# headers = {
# 	"X-RapidAPI-Key": "ddf7f8bf8dmsh84d004767cd55a6p1453f1jsn361373ff356b",
# 	"X-RapidAPI-Host": "football98.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)


import requests

url = "https://football98.p.rapidapi.com/brasileirãosériea/news"

headers = {
	"X-RapidAPI-Key": "92d6013870mshf4429f4c7f7a700p103b4ejsnb48d7a735a37",
	"X-RapidAPI-Host": "football98.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

json = json_normalize(response.json())

print(json)
