import requests

url = "https://v6.exchangerate-api.com/v6/dh/"
params = "latest/USD"
response = requests.get(url+params)
data = response.json()['conversion_rates']['UZS']
print(data)


params = "pair/USD/RUB"
response = requests.get(url+params)
data = response.json()['conversion_rate']
print(data)

