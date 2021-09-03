import requests

# Docs for requests module: https://docs.python-requests.org/en/master/
# https://realpython.com/python-requests/

# ISS Location API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(f"Response Code = {response.status_code}")
print(f"Response Text = {response.text}")

response_data = response.json()  # This is a dict
latitude = response_data['iss_position']['latitude']
longitude = response_data['iss_position']['longitude']
iss_position = (latitude, longitude)

print(f"ISS Position = {iss_position}")

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# If the response was successful, no Exception will be raised
response.raise_for_status()
