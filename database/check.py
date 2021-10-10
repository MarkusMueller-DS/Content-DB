import pandas as pd
import os

folder_path = "/Users/markusmuller/python/projects/content-db"

df = pd.read_csv(os.path.join(folder_path, 'gmail/data/KDnuggets/KDnuggets_data.csv'))
# print(df.info())

url_list = df['url'].values.tolist()
title_list = df['title'].values.tolist()
summary_list = df['summary'].values.tolist()
content_list = df['content'].values.tolist()
tag_list = df['tag'].values.tolist()

# print(url_list[777])
# print(title_list[777])
# print(summary_list[777])
# print(content_list[777])
# print(tag_list[777])

print(df.info())
print(tag_list[777])

print(url_list[777])
print(url_list[778])
print(title_list[778])
