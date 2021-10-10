# script to check for new items that are saved to pocket

import pickle
import datetime
import pocket_api_tokens
import requests


# get access tokens from secret file
con_key = pocket_api_tokens.consumer_key
access_token = pocket_api_tokens.access_token

# access_token has more information that isnt needed for the request
sep = '&'
stripped_token = access_token.split(sep, 1)[0]

date_string = "09.28.2021"
date = datetime.datetime.strptime(date_string, "%m.%d.%Y")
timestamp = datetime.datetime.timestamp(date)
print(timestamp)



# define query parameters
parameters = {"consumer_key": con_key, "access_token":stripped_token, "since":"1633860421"}

# make the request
r = requests.get("https://getpocket.com/v3/get", params=parameters)

#print(con_key)
#print(access_token)
r = r.json()


# show the result
# check if list if retured list is empty or not
if r['list']:
    print("new items")
else:
    print("no new items")

# date_ = datetime.date.today().strftime("%m.%d.%Y")
# filename = 'pocket_lastquery.pkl'

# with open('data/'+ filename, 'wb') as f:
    # pickle.dump(txt, f)

# with open('data/'+filename, 'rb') as f:
    # file = pickle.load(f)

# print(file)
