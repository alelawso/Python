import requests

url = "http://api.weatherapi.com/v1/current.json?key=1f8c820e6e7f4d41bed160029232606&q=Burns Harbor&aqi=no"
response = requests.get(url) ##use get method to avoid error
weather_json =  response.json()

##nested dictionaries in json
time = weather_json.get("current").get("last_updated")
location = weather_json.get("location").get("name")
state = weather_json.get("location").get("region")
temp = weather_json.get("current").get("temp_f")
humidity = weather_json.get("current").get("humidity")
feelslike = weather_json.get("current").get("feelslike_f")
desc = (weather_json.get("current").get("condition").get("text")).lower()

print("In", location, state, ", as of", time, "it is", desc, "and the temperature is", temp, "° fahrenheit.  The humidity is", humidity, "% and it feels like", 
    feelslike, "° outside.")