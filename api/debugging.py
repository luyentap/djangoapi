import requests
import json

response = requests.get('https://django-api-2-gaga2017.c9users.io/api/v1/product/')
event = json.loads(response.content)
print(event)
print("A")


# del event['id'] # We want the server to assign a new id

# response = requests.post('https://django-api-2-gaga2017.c9users.io/api/v1/product/',
#                          data=json.dumps(event),
#                          headers={'content-type': 'application/json'})