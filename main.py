import requests
response=requests.get("https://www.python.org",timeout=20)
print(response.status_code)

