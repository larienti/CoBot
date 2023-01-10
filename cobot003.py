from coinbase.wallet.client import Client
import json, os

api_key = os.getenv('API_KEY')
client = Client(api_key)

accounts = client.get_accounts()
for account in accounts.get("data"):
  print("Account ID: ", account.get("id"))
  print("Account Name: ", account.get("name"))
  print("Account Balance: ", account.get("balance").get("amount"), account.get("balance").get("currency"))