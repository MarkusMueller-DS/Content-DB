import os
import pickle
import pandas as pd
import requests
import bs4 as BeautifulSoup

data_path = '/Users/markusmuller/python/projects/content-db/gmail/data/KDnuggets/'

with open(os.path.join(data_path, 'KDnuggets_valid_urls.pkl'), 'rb') as f:
    valid_urls = pickle.load(f)

# print(valid_urls[1])

# function to get content from KDnuggets
def queryData(links):
    title_list = []
    summary_list = []
    content_list = []
    url_list = []
    error_list = []

    # for loop to get title and summary
    for c, url in enumerate(links):
        print(c)
        page = requests.get(url)
        soup = BeautifulSoup.BeautifulSoup(page.content, "html.parser")
        print(c)

        try:
            if soup.find(id="post-header") != None:
                title = soup.find(id="post-header").find(id="title")
                summary = soup.find(id='post-header').find(class_='excerpt')
            else:
                title = soup.find(id="title")
                summary = soup.find(class_="excerpt")

            title = title.text.strip()
            summary = summary.text.strip()
            content = soup.find(id="post-").text.strip()

        except:
            print('unexpected error url is added to error_list')
            error_list.append(url)


        title_list.append(title)
        summary_list.append(summary)
        content_list.append(content)
        url_list.append(url)

    df_new = pd.DataFrame()
    df_new['link'] = url_list
    df_new['title'] = title_list
    df_new['summary'] = summary_list
    df_new['content'] = content_list

    return df_new


# check if there was a prev query
if os.path.exists(os.path.join(data_path, 'content_KDnuggets.csv')):
    df = pd.read_csv(data_path + 'content_KDnuggets.csv')
    # print(df.info())
    # get list of links that are already in the db
    queried_links = df['link'].values
    # print(queried_links)
    links_to_query = list(set(valid_urls) - set(queried_links))
    # print(len(links_to_query))
    df_new_query = queryData(links_to_query)

    frames = [df, df_new_query]
    df_final = pd.concat(frames)

    df_final.to_csv(os.path.join(data_path, 'content_KDnuggets.csv'), index=False)
    df_final.info()

