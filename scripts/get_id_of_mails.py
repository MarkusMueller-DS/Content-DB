# imports
from google.oauth2.credentials import Credentials   # handel auth
from googleapiclient.discovery import build         # used to make the queries

import pickle                   # save raw data from query
import datetime


# save date and time of query to the next time I can query new mails
date_ = datetime.date.today().strftime("%m/%d/%Y")
date = date_.replace('/', '.')
query_name = 'id_query_' + date + ".pkl"

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
result = service.users().messages().list(userId='markus.mueller.ds@gmail.com', q='after:09/17/2021', maxResults=500).execute()

# save raw data in a pickle file
outfile = open(query_name, 'wb')
pickle.dump(result, outfile)
outfile.close()

# save date of last query to load it in the next time and use it as the new q parameter in list()
outfile = open('lastquery.pkl', 'wb')
pickle.dump(date, outfile)
outfile.close()
