import requests
import json
movie_names = ["The Devil Wears Prada", "ironman"]
movies = []
for n , name in enumerate(movie_names):
    res = requests.get("http://www.omdbapi.com/?apikey=XXXXXX&t={}".format(movie_names[n]))
    movies.append(res.json())
    # print(n)
    # print(name)
    # print("=====")

titles = []
years = []
directors = []
for x in movies:
    titles.append(x["Title"])
    years.append(x["Year"])
    directors.append(x["Director"])
# print(Title)
# print(Year)
# print(Director)

movies2 = []
for s in range(len(titles)):
    movies2.append({"titles":titles[s],"years":years[s],"directors":directors[s]})
print(movies2)

file_name = "movie.json"
with open(file_name,"a") as file_object:
    for i in movies2:
        json.dump(i,file_object)