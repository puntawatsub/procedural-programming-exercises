import requests

def task1():
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    result = response["value"]
    print(result)

def task2():
    city_name = input("City Name: ")
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", {"q": f"{city_name}", "appid": "3e25a93cdfe6ba5719e510f19787f54a"}).json()
    print(f"Description: {response['weather'][0]['description']}, Temperature: {float(response['main']['temp']) - 272.15:.2f}°C")
    

if __name__ == "__main__":
    # task1()
    task2()