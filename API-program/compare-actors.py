from dotenv import load_dotenv
import os
import requests
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

#Id numbers for tv show credits to compare - gotten from TMDB
id1 = 4057
id2 = 1416

#Urls to tell TMDB what data to give you. Here: Aggregate credits (list of everyone credited on the shows)
url1 = f"https://api.themoviedb.org/3/tv/{id1}/aggregate_credits?language=en-US"
url2 = f"https://api.themoviedb.org/3/tv/{id2}/aggregate_credits?language=en-US"

#Tells TMDB the data type the response should be, and tells them that you are an authorised user
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('FILM_API_TOKEN')} "
}

#Gets the response from TMDB
response1 = requests.get(url1, headers=headers)
response2 = requests.get(url2, headers=headers)

#Turns the json response into dictionaries usable in python
data1 = response1.json()
data2 = response2.json()

#Dictionaries for storing the actors and their info
double = {}
doublesignificant = {}

#Checks if the actors in show 1 are in show 2, and adds them to a dictionary with their name, episode counts, and roles
for people1 in data1["cast"]:
    for people2 in data2["cast"]:
        if people2["name"] == people1["name"] and people1["known_for_department"] == "Acting":
            try:
                double[people1["name"]] = {"episode count": [people1["total_episode_count"], people2["total_episode_count"]], "roles":[people1["roles"][0]["character"], people2["roles"][0]["character"]]}
            
            except KeyError:
                print("KeyError")

#Checks if the actor has been featured in multiple episodes on both shows, and adds them if so
for people in double:
    if double[people]["episode count"][0] > 1 and double[people]["episode count"][1] > 1:
        doublesignificant[people] = double[people]

#Prints the dictionary of returning actors on both shows
print(doublesignificant)
