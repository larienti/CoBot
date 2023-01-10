import json, hmac, hashlib, time, requests, os
from requests.auth import AuthBase

# Before implementation, set environmental variables with the names API_KEY and API_SECRET
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Create custom authentication for Coinbase API
class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))
        message = timestamp + request.method + request.path_url + (request.body or '')
        signature = hmac.new(self.secret_key, message, hashlib.sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
        })
        return request

api_url = 'https://api.coinbase.com/v2/'
auth = CoinbaseWalletAuth(API_KEY, API_SECRET)

# Get current user
r = requests.get(api_url + 'user', auth=auth)
print r.json()
# {u'data': {u'username': None, u'resource': u'user', u'name': u'User'...

# Send funds
tx = {
    'type': 'send',
    'to': 'user@example.com',
    'amount': '10.0',
    'currency': 'USD',
}
r = requests.post(api_url + 'accounts/primary/transactions', json=tx, auth=auth)
print r.json()
# {u'data': {u'status': u'pending', u'amount': {u'currency': u'BTC'...