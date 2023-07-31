
# importing requests and json
import requests, json

# ********* WARNING !!! DO NOT MODIFY THIS PART OF CODE *********
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "b20008d401611e721958b2a99dcf4a67"
# ***************************************************************


print("\n\t\t\t\t********* WELCOME TO MY WEATHER APP PROJECT *********\n")
CITY = input("Please enter the name of city you want to check weather:\t").strip()

# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY;       CITY = " " + CITY.upper() + " "

# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']

   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
    
   # weather report
   report = data['weather']

   print(f"\n\nShowing Weather of: {CITY:-^30}")
   print(f"\nTemperature: {temperature - 271:.2f}° celsius")
   print(f"\nFeels like: {main['feels_like'] - 271:.2f}° celsius")
   print(f"\nMaximum temperature: {main['temp_max'] - 271:.2f}° celsius")
   print(f"\nMinimum temperature: {main['temp_min'] - 271:.2f}° celsius")
   print(f"\nHumidity: {humidity}% (g.m-3)")
   print(f"\nPressure: {pressure} millibars")
   print(f"\nVisibility: {data['visibility']} statute miles")
   print(f"\nWind Speed: {data['wind']['speed']} kmph")
   print(f"\nWeather Report: {report[0]['description']}")
   print(f"\nCountry Code: {data['sys']['country']}")
   print(f"\n\t\t\t\t********* THANK YOU VISIT AGAIN *********\n")

elif response.status_code == 404:
   print("\nCity not found, status_code:", response.status_code, "\tPlease enter a valid city name...")
else:
   print("\nError in the HTTP request, status_code:", response.status_code)