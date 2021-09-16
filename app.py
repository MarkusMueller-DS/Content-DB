from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path
import base64
import email
from bs4 import BeautifulSoup

# Define SCOPES
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def getEmails():
    # check if token.json is located in pwd
    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        result = service.users().messages().list(userId='markus.mueller.ds@gmail.com').execute()
        messages = result.get('messages')
        txt = service.users().messages().get(userId='markus.mueller.ds@gmail.com', id='17beb2ea7a06eb5e').execute()
        print(type(txt))
        print(txt.keys()) 
        print(txt['payload'])
        
        # iterate through all the messages
       #  for msg in messages:
       #      # Get the message from its id
       #      txt = service.users().messages().get(userId='markus.mueller.ds@gmail.com', id=msg['id']).execute()

       #      # Use try-except to avoid any Errors
       #      try:
       #          # Get value of 'payload' from dictionary 'txt'
       #          payload = txt['payload']
       #          headers = payload['headers']

       #          # Look for Subject and Sender Email in the headers
       #          for d in headers:
       #              if d['name'] == 'Subject':
       #                  subject = d['value']
       #              if d['name'] == 'From':
       #                  sender = d['value']

       #          # The Body of the message is in Encrypted format. So, we have to decode it.
       #          # Get the data and decode it with base 64 decoder.
       #          parts = payload.get('parts')[0]
       #          data = parts['body']['data']
       #          data = data.replace("-","+").replace("_","/")
       #          decoded_data = base64.b64decode(data)

       #          # Now, the data obtained is in lxml. So, we will parse
       #          # it with BeautifulSoup library
       #          soup = BeautifulSoup(decoded_data , "lxml")
       #          body = soup.body()

       #          # Printing the subject, sender's email and message
       #          print("Subject: ", subject)
       #          print("From: ", sender)
       #          print("Message: ", body)
       #          print('\n')
       #      except:
       #          pass
                
    except ValueError:
       print("no token file in pwd, init quickstart to create the file")
    
getEmails() # iterate through all the messages
