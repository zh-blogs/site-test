import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

with open('data.json', 'r', encoding='utf8') as json_file:
    json_data = json.load(json_file)
    
for index in range(len(json_data["data"]["blogs"])):
    print("Checking:", json_data["data"]["blogs"][index]["url"], end = " ")
    try:
        res = requests.get(json_data["data"]["blogs"][index]["url"], timeout=5, headers=headers)
        if res.status_code != 200:
            json_data["data"]["blogs"][index]["status"] = res.status_code
            print("[", res.status_code,"]")
    except Exception as e:
        json_data["data"]["blogs"][index]["status"] = str(type(e)).split("'")[1].split(".")[2]
        print("[", json_data["data"]["blogs"][index]["status"],"]")
