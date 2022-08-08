import requests

list = []
res = requests.get("https://api.cnyes.com/media/api/v1/newslist/category/headline?startAt=1648656000&endAt=1649606399&limit=30")
data = res.json()
data_list = data["items"]["data"]

for x in data_list:
    list.append(x["title"])
print(list)