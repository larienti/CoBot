import http.client
import json

conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", "/accounts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

$ C:/Python38/python.exe c:/Coding/CoBot/cobot002coinbassapi.py
{"message":"User-Agent header is required."}