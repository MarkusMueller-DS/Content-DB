# imports
from google.oauth2.credentials import Credentials   # handel auth
from googleapiclient.discovery import build         # used to make the queries

import pickle                   # save raw data from query


# Define SCOPES
# relevant for auth
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
pathToToken = '/Users/markusmuller/python/projects/gmail-newsletter-db/token.json'
creds = Credentials.from_authorized_user_file(pathToToken, SCOPES)

# connect to Gmail api
service = build('gmail', 'v1', credentials=creds)

# request a list of all the messages
# maxResult is limited to 500
# with nextPageToken (will be in the result dict) we can continue to get mail_ids
# if non nextPageToken is in the result dict then we reached the end of our mailbox
result = service.users().messages().list(userId='markus.mueller.ds@gmail.com', maxResults=500, pageToken='12641347343635093789').execute()

# save raw data in a pickle file
filename = 'id_query_17.09.2021_q3'
outfile = open(filename,'wb')
pickle.dump(result, outfile)
outfile.close()


