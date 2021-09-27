import json
import pandas as pd
import requests
import pocket_api_tokens


# get access tokens from secret file
con_key = pocket_api_tokens.consumer_key
access_token = pocket_api_tokens.access_token

# access_token has more information that isnt needed for the request
sep = '&'
stripped_token = access_token.split(sep, 1)[0]

# define query parameters
parameters = {"consumer_key": con_key, "access_token":stripped_token, "count":"2"}

# make the request
r = requests.get("https://getpocket.com/v3/get", params=parameters)

#print(con_key)
#print(access_token)

# show the result
print(r.json())

