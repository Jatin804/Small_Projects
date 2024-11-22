import requests

class VariablesKeys:
    API_KEY = "(api_key)"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

class WeatherSys:

    def __init__(self, city=""):
        self.city = city

    def get_weather(self):
        url = f"{VariablesKeys.BASE_URL}q={self.city},IN&appid={VariablesKeys.API_KEY}&units=metric"
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract weather information
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            sys = data['sys']
            
            # Print weather details
            print(f"Weather in country: {sys['country']}, city: {self.city} :")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Weather: {weather['description']}")
            print(f"Wind Speed: {wind['speed']} m/s")

        else:
            print("City not found or API error.")

# Input city name
city = input("Enter your proper city name with correct spelling: ")
obj = WeatherSys(city)
obj.get_weather()
