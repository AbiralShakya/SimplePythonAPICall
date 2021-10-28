import requests as re 

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint + query 

response = re.get(url)

breeds = response.json()["message"]
#bulldogs = breeds.get("bulldog")
#print(bulldogs)

all_breeds = breeds.keys()
for breed in all_breeds:
  print(breed)

#get list of all subbreeds of breed with at least 3 sub-breeds 

hounds = breeds["hound"]
input("\nPress enter to get all hound subbreeds")
for hound in hounds:
  print(hound)

