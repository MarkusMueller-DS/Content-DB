from google.oauth2.credentials import Credentials   # handel auth
from googleapiclient.discovery import build         # used to make the queries
import os                       # handle paths
import base64                   # decrypt mail data
from bs4 import BeautifulSoup   # parse data after decryption
import pickle
import datetime
import pandas as pd


search_str = "from:lon@dataelixir.com"
filename = "dataelixir_ids_"
date = datetime.date.today().strftime("%m.%d.%Y")
filename = filename + date + ".pkl"
# print(filename)

pathToToken = '/Users/markusmuller/python/projects/content-db/gmail/token.json'
data_path   = '/Users/markusmuller/python/projects/content-db/gmail/data/dataelixir'

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = Credentials.from_authorized_user_file(pathToToken, SCOPES)

# connect to Gmail api
service = build('gmail', 'v1', credentials=creds)

# request a list of all the messages
result = service.users().messages().list(userId='markus.mueller.ds@gmail.com', q=search_str, maxResults=500).execute()

with open(os.path.join(data_path, filename), 'wb') as f:
    pickle.dump(result, f)
