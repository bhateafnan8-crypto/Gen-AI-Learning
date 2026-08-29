"""
=== Weather CLI App ===

Features:
  - City name lo user se
  - Real API se weather fetch karo
  - Data display karo (temp, condition, humidity)
  - Result JSON file mein save karo
  - Regex se city name validate karo

---- API ----
  wttr.in — free, no key required
  URL: https://wttr.in/{city}?format=j1

---- Structure ----
  - validate_city()  → regex se input check
  - fetch_weather()  → API call + error handling
  - display_weather() → formatted print
  - save_to_json()   → JSON file mein save
  - main()           → loop + input

---- Topics Covered ----
  - requests   → API call
  - JSON       → parse + save
  - Regex      → city validation
  - Error handling → timeout, 404, connection
  - File handling → JSON save
  - os         → file path
"""

# code start here

#  all imports module
import json
import re
import os
import requests

city_name = input("Enter your city name to get weather : ").strip()

# validation of city
def validate_city(city_name):
    patern = r"^[A-Za-z][A-Za-z\s\-\.']{1,49}$"

    return bool(re.match(patern,city_name))

# fetch weather
def fetch_weather(city1):
    if not validate_city(city1):
        print("Invalid city")
        return None
    try:
        # validate = validate_city(city_name)

        file = requests.get(f"https://wttr.in/{city1}?format=j1",timeout=10)

        file.raise_for_status()

        print(f"status code : {file.status_code}")

        return file.json()

    except requests.exceptions.ConnectionError:
        print("Error : (Connection Failed)")

    except requests.exceptions.Timeout:
        print(" Error : (Timout)")

    except requests.exceptions.RequestException as e:
        print(f"Error : ({e})")

# display weather
def display_weather(city2):
    fetch1 = fetch_weather(city2)

    if fetch1:
        current = fetch1['current_condition'][0]
        temp = current['temp_C']
        condition = current['weatherDesc'][0]['value']
        humidity = current['humidity']

        return (f"{city2} => temp : {temp} |  condition : {condition} | humidity : {humidity}%")

#  save to json
def save_to_json():

    disp = display_weather(city_name)
    print(disp)
    filename = input("Enter filename to save (without extension) : ").strip()

    if os.path.exists(filename):
        print("File already exist..")
    else:
        print(f"Creating new file : {filename}")
    with open(filename+".json","w") as file:
        json.dump({"result":disp},file,indent=4)

    print(f"Save data to {filename} successfully")

#  main running
def main():
    save_to_json()

#  __name__ == "__main__"
if __name__ == "__main__":
    main()


#  galat hai ...

    # import json
    # import re
    # import os
    # import requests

    # city_name = input("Enter your city name to get weather : ").strip()

    # def validate_city(city):
    #     patern = r"^[A-Za-z][A-Za-z\s\-\.']{1,49}$"

    #     return bool(re.match(patern,city))

    # def fetch_weather(city1):
    #     try:
    #         validate = validate_city(city_name)

    #         file = requests.get(f"https://wttr.in/{city1}?format=j1",timeout=10)

    #         file.raise_for_status()

    #         print(f"status code : {file.status_code}")

    #         fetch = file.json()

    #         if validate:
    #             return fetch
    #         else:
    #             print("Not found")

    #     except requests.exceptions.ConnectionError:
    #         print("Connection Failed")
    #     except requests.exceptions.ConnectTimeout:
    #         print("Timout")
    #     except requests.exceptions.Timeout:
    #         print("Timout Error")
    #     except requests.exceptions.BaseHTTPError:
    #         print("404")
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error : {e}")

    # def display_weather(city2):

    #     fetch1 = fetch_weather(city_name)

    #     if fetch1:
    #         return (f"{city2} => temp : {fetch1['temp']} |  condition : {fetch1['condition']} | humidity : {fetch1['humidity']}")


    # def save_to_json():

    #     disp = display_weather(city_name)

    #     with open("weather.json","w") as file:
    #         file.writable(file,disp)


# weather.py