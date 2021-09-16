from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path
import base64
import email
from bs4 import BeautifulSoup
import json

# Define SCOPES
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def getEmailsList():
    # check if token.json is located in pwd
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)
 
    result = service.users().messages().list(userId='markus.mueller.ds@gmail.com').execute()
    # print(len(result))
    # print(result)
    
    with open('mailList.txt','w') as file:
        file.write(json.dumps(result))
    
getEmailsList()
