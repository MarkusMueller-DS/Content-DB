# Script from: https://medium.com/@alexdambra/getting-your-reading-history-out-of-pocket-using-python-b4253dbe865c
# Pocket API: https://getpocket.com/developer/docs/authentication
# can be used to the access token from the pocket api


import json
import requests
import pocket_api_tokens
from urllib.parse import urlencode
from urllib.request import Request, urlopen

con_key = consumer_key.consumer_key
request_token = consumer_key.request_token
#url = "https://getpocket.com/v3/oauth/request"

#post_fields = {"consumer_key":consumer_key, "redirect_uri": "http://www.google.com"}

#request = Request(url, urlencode(post_fields).encode())
#json = urlopen(request).read().decode()

#print(json)


# POST request an access token
url = "https://getpocket.com/v3/oauth/authorize"
post_fields = {"consumer_key":con_key, "code":request_token}

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()

print(json)
