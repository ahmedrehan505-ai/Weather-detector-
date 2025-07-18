import requests

def get_weather(Lahore, apd89239dec3b1fa257a216f2d1a429fe0
):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found or API issue.")
        print("Error:", data.get("message"))
        return

    print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

# Replace this with your actual API key
api_key = "d89239dec3b1fa257a216f2d1a429fe0"

# Get city name from user input
city = input("Enter city name: ")

# Call the function
get_weather("Lahore", "apd89239dec3b1fa257a216f2d1a429fe0"
)
