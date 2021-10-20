# Content Database
##### by Markus Müller

## Problem
- I am following multiple newsletters, actively saving interesting articles to pocket or medium. Now I am at the point where I have no overview over all the articles and blog posts.
- Especially my mailbox is overflowing with possibly relevant information

## Goal
- have one place where everything is saved so it is easier to search through it and find interesting stuff
- create a sql-Database which is automatically updated 
- combine everything in one web app (Django)

### Files
- Notebooks are WIP and are, for now, only for testing purposes


### Progress
- [ ] Flask Web App
    - [x] create web app
    - [ ] add search function 
    - [ ] design web page
- [ ] Database
    - [x] create a test database
    - [x] combine results in one database:
        - currently combined: articles form KDnuggets, Dataelixir and Pocket
- [ ] Gmail
    - [x] connected to the api
    - [x] queried ids of mails
    - [ ] developed a parser to get the content of the mails 
        - [ ] KDnuggets
            - [x] explore how to get the relevant informations
            - [x] create script to get ids
            - [x] create script to get data
        - [ ] DeepLearning AI
        - [ ] PyCoder's Weekly
        - [ ] Data Elixir
            - [x] get data
            - [ ] parse data
        - [ ] DeepAI
        - [ ] ML Mastery
    - [ ] meta data and content from each mail 
- [ ] Pocket
    - [x] connected to the api
    - [x] made first request
    - [x] query the articles 
    - [ ] write a script to collect data 
- [ ] Medium
    - [ ] look for ways the get the data from medium
    - ...
- [ ] Youtube saved videos
    - [ ] connect to the api
    - [ ] get saved videos
    - [ ] write a script to collect data
- [ ] Twitter saved tweets
    - [x] connect to the api -> API dose not allow to access saved tweets
    - [ ] check possibility to get data through selenium
    - [ ] get saved tweets
    - [ ] write a script to collect data

