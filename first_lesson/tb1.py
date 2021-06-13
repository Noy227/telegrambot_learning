import requests

API_LINK = "https://api.telegram.org/bot1891929353:AAF1rtsB276-XrsZiSVj2Idc2YEtO9A7CS8"

updates = requests.get(API_LINK + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_LINK + f"/sendMessage?chat_id={chat_id}&text=Блабла{text}блабла")