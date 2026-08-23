import json
import requests

def main():

    
    try:
        url = 'https://api.open-meteo.com/v1/forecast?latitude=21.4901&longitude=39.1862&hourly=temperature_2m'
        weather = requests.get(url)
        data =  weather.json()
        # time, tem = data["hourly"]["temperature_2m"][0]
        day, hour = data["hourly"]["time"][0].split('T')


        
        print(f"Date: {day} | Time: {hour} | Temp: {data["hourly"]["temperature_2m"][0]}°C")
        # print(data['longitude'])
        # print(json.dumps(data, indent=2))
        # print(json.dumps(data['hourly'], indent=2))


    except:
        print('errer')

main()