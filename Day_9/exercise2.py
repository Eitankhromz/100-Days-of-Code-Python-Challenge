travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#Do NOT change the code above

#Write the function that will allow new countries
#to be added to the travel_log

def add_new_country(country, visits, list_of_places):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = list_of_places
    travel_log.append(new_dict)
        


#Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



for dict in travel_log:
    all_places = ""
    country = dict["country"]
    times = dict["visits"]
    places = dict["cities"]
    for city in places:
        if places.index(city) == len(places) - 1:
            all_places+= "and " + city
        elif places.index(city) < len(places) - 1:
            all_places+= city + ", "
    print(f"You've visited {country} {times} times.")
    print(f"You've been to {all_places}.")
    

