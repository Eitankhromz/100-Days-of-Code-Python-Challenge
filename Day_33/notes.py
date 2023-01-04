import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# #Shows response status code
# print(response.status_code)

#Raises Exception Errors
response.raise_for_status()

#STATUS CODES
# 1XX - 'HOLD ON'
# 2XX - 'HERE YOU GO (SUCCESS)'
# 3XX - 'YOU DONT HAVE ACCESS (GO AWAY)'
# 4XX - 'YOU SCREWED UP'
# 5XX - 'SERVER SCREWED UP'

#Retrieving JSON data
data = response.json() #imports JSON data as a dictionary so can tap into any key i.e [iss_position]

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

