import requests
from datetime import datetime, timezone
import smtplib
import time

# Docs for this API: https://sunrise-sunset.org/api

URL = "https://api.sunrise-sunset.org/json"
LATITUDE_PARAM = "lat"
LONGITUDE_PARAM = "lng"
FORMATTED_PARAM = "formatted"
LATITUDE_VALUE = 25.594095  # From https://www.latlong.net/
LONGITUDE_VALUE = 85.137566


def is_location_near_me(latitude, longitude):
    degrees_delta = 5
    latitude_min = LATITUDE_VALUE - degrees_delta
    latitude_max = LATITUDE_VALUE + degrees_delta
    longitude_min = LONGITUDE_VALUE - degrees_delta
    longitude_max = LONGITUDE_VALUE + degrees_delta

    return (latitude_min <= latitude <= latitude_max) and (longitude_min <= longitude <= longitude_max)


def is_iss_overhead():
    # ISS position API
    iss_position_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_position_response.raise_for_status()

    iss_position_response_data = iss_position_response.json()
    iss_latitude = float(iss_position_response_data['iss_position']['latitude'])
    iss_longitude = float(iss_position_response_data['iss_position']['longitude'])
    # print(f"ISS Position: {iss_latitude}, {iss_longitude}")

    # ISS doesn't have to be directly over my (lat, lng). It can be within +5 or -5 degrees of my position.
    return is_location_near_me(iss_latitude, iss_longitude)


def is_night_now():
    parameters = {
        LATITUDE_PARAM: LATITUDE_VALUE,
        LONGITUDE_PARAM: LONGITUDE_VALUE,
        FORMATTED_PARAM: 0,
    }

    # Sunrise-Sunset API
    sunrise_sunset_api_response = requests.get(url=URL, params=parameters)
    sunrise_sunset_api_response.raise_for_status()

    sunrise_sunset_data = sunrise_sunset_api_response.json()

    sunrise_hour = int(sunrise_sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sunrise_sunset_data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(f"Sunrise = {sunrise_hour}, Sunset = {sunset_hour}")

    # Current time: As the time returned by Sunrise/Sunset API is in UTC, not local, we will use the same
    hour_now = datetime.now(timezone.utc).hour
    return hour_now <= sunrise_hour or hour_now >= sunset_hour


def send_email(email_subject, email_body):
    my_email = "my_email@gmail.com"  # Update email
    password = "my_password"  # Update password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:{email_subject}\n\n{email_body}"
        )


while True:
    # If the ISS is close to my current position, and it is currently dark, then send me an email
    if is_iss_overhead() and is_night_now():
        send_email("Look up!", "The ISS is above you in the sky.")

    time.sleep(60)  # Sleep for 60 seconds
