programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }
#Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

#create an empty dictionary
new_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an existing entry
# programming_dictionary["Bug"] = "A moth in you computer"
# print(programming_dictionary)

#Loop thru a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting List in Dictionary
# travel_log = {
#     "USA": ["Washington", "Los Angeles", "New York"],
#     "Canada": ["Toronto", "Montreal", "Alberta"],
# }

#Nesting Dictionary in Dictionary
travel_log = {
    "USA": {
            "cities_visited": ["Washington", "Los Angeles", "New York"],
            "total_visited": 12
            },
    "Canada": {
                "will_visit": ["Toronto", "Montreal", "Alberta"], 
                "total": 3 
                },
     
}

#Nesting Dictionary in List
travel_log = [
    {
        "country": "USA", 
        "cities_visited": ["Washington", "Los Angeles", "New York"], 
        "total_visited": 12},
    {
        "country": "Canada", 
         "will_visit": ["Toronto", "Montreal", "Alberta"], 
         "total": 3 },
]
print(travel_log)
