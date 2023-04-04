import requests as http_client
from twilio.rest import Client

api_key = "60c7204f243373ddb5d2535748b04a0b"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 44.902220,
    "lon": 10.537130,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Twilio credentials
account_sid = "AC677fb071aa635f51fb6fe9aa9f636ba9"
auth_token = "778f56cb535ba892f1d4a9ea4cfe6d86"
twilio_phone_number = "+15856327098"


def get_my_city_weather():
    global api_key, OWM_Endpoint, weather_params
    response = http_client.get(OWM_Endpoint, params=weather_params)
    print(f"Status Code: {response.status_code}")
    response.raise_for_status()
    return response.json()


weather_data = get_my_city_weather()
print(weather_data)

weather_ids = []

for hour_data in weather_data["hourly"][:12]:
    weather_ids.append(hour_data["weather"][0]["id"])


if any([weather_id < 700 for weather_id in weather_ids]):
    print("Compà, ci sta 'a pioggia")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Compà, ci sta \'a pioggia oje, pigghia l\'☂️',
        from_=twilio_phone_number,
        to='+393534181940'
    )

    print(message.status)
