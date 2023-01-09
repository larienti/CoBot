import requests

url = "https://web-api.ampleforth.org/eth/token-info"
response = requests.get(url)

if response.status_code == 200:
    # Success!
    data = response.json()
    print(data)
else:
    # There was an error
    print("Error:", response.status_code)