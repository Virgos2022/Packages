import requests

url = "https://v2.jokeapi.dev/joke/Any?safe-mode"

response = requests.get(url)
# print(response)

recieved_data=response.json()
# print(recieved_data["category"])

for x in recieved_data.keys():
    if(x == "id" or x=="type" or x == "flags" or x == "error"):
        continue
    print("{} : {}".format(x,recieved_data[x]))