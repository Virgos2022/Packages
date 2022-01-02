import requests

url = "https://currencyapi.net/api/v1/rates?key=MPVC4v1Ac1Dq0otQI72HLxxqqZpAsamPbhBW&output=json"


response = requests.get(url)
print(response)
# print(response.text)
data=response.json()

for x in data.keys():
    if x == "rates":
        currency_data=data["rates"]
        for d in currency_data.keys():
            if d == "INR":
                lk = currency_data[d]
                break

user_input = int(input("Enter Amount In Dollars"))
k = user_input * lk
print("The Dollars when converted in Indian rupee is: {}".format(k))            

   
