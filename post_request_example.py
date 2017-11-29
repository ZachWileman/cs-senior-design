import requests

URL = 'http://localhost:8000/notifications/'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
csrftoken = client.cookies['csrftoken']

notification_data = {
    'attack': 'Christmas Tree Attack',
    'dest_address': '123.12.32.12',
    'source_address': '123.123.123.123',
    'threat_level': 'Severe',
    'csrfmiddlewaretoken': csrftoken,
}

r = client.post(URL, data=notification_data)
print(r.text)
