import requests as re 

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint + query 

response = re.get(url)

print(response.json())