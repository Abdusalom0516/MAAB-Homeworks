import requests

response = requests.get("https://www.youtube.com/watch?v=BsBDB11nl1Y&list=RDVkYkqISa69Y&index=25")

if response:
    print(response.content)
else:
    print(response.status_code)