import requests

URL = 'http://localhost:8000/notifications/'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
csrftoken = client.cookies['csrftoken']

notification_data = {
    'description': 'Here is a new description',
    'mac_address': 'MM:MM:MM:SS:SS:SS',
    'csrfmiddlewaretoken': csrftoken
}

r = client.post(URL, data=notification_data)
print(r.text)
