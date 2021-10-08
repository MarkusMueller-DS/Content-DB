from google.oauth2.credentials import Credentials   # handel auth
from googleapiclient.discovery import build         # used to make the queries
import os                  # handle paths
import pickle
import datetime
import pandas as pd

data_path = "/Users/markusmuller/python/projects/content-db/gmail/data/dataelixir"
token_path = '/Users/markusmuller/python/projects/content-db/gmail/token.json'

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = Credentials.from_authorized_user_file(token_path, SCOPES)
service = build('gmail', 'v1', credentials=creds)

# read in ids to query
with open(os.path.join(data_path, 'dataelixir_ids_10.08.2021.pkl'), 'rb') as f:
    ids = pickle.load(f)

id_list = []
for id_ in ids['messages']:
    id_list.append(id_)

# get mails with ids in id_list
mail_list = []
for id_ in id_list:
    mail = service.users().messages().get(userId='me', id=id_['id']).execute()
    mail_list.append(mail)


with open(os.path.join(data_path, 'mails.pkl'), 'wb') as f:
    pickle.dump(mail_list, f)

print(len(mail_list))

