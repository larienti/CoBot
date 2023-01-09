from coinbase.wallet.client import Client
import json

client = Client("api_key", "api_secret", "password")

orders = client.orders.list()

for order in orders:
    print("ID: ", order.id)
    print("Price: ", order.price)
    print("Size: ", order.size)
    print("Product ID: ", order.product_id)
    print("Side: ", order.side)
    print("Status: ", order.status)
    print("\n")
    
    
    C:\Python38\lib\site-packages\coinbase\wallet\util.py:45: 
        UserWarning: WARNING: this client is sending a request to an insecure API endpoint. 
        Any API request you make may expose your API key and secret to third parties.
    Consider using the default endpoint:
        
  password

  warnings.warn(warning_message, UserWarning)
Traceback (most recent call last):
  File "c:/Coding/CoBot/cobot003.py", line 6, in <module>
    orders = client.orders.list()