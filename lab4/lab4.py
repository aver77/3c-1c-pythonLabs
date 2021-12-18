import requests
# import csv
# from bs4 import BeautifulSoup
from datetime import datetime

def getAllPosts():
    token = '7391472f7391472f7391472fd573eb32ce773917391472f122720cc5f6b4ac6ee790dcb'
    version = 5.92
    domain = 'myprotein36'
    all_posts = []
    count = 100
    offset = 100
    
    response = requests.get('https://api.vk.com/method/wall.get', params={
        'access_token': token,
        'v': version,
        'domain': domain,
        'count': count
    })

    data = response.json()['response']['items']
    all_posts.extend(data)

    while len(data) > 0:
        response = requests.get('https://api.vk.com/method/wall.get', params={
            'access_token': token,
            'v': version,
            'domain': domain,
            'count': count,
            'offset': offset
        })

        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 100
    
    return all_posts

def getAllLikes(data):
    likes = 0
    for i in data:
        likes+=i['likes']['count']
    
    return likes

def writeInTxt(likes, listDate, listLikes):
    with open('test.txt', 'w') as file:
        file.write('Total number of likes: ' + str(likes) + '\n')
        file.write('General daily active in likes: \n')
        for i in range(0,len(listDate)):
            file.write(listDate[i] + ' : ' + str(listLikes[i]) + '\n')

allPosts = getAllPosts()
allLikes = getAllLikes(allPosts)
print('Общее число постов:', len(allPosts))
print('Общее число лайков:', allLikes)

listDate = []
listLikes = []
for i in allPosts:
    date = datetime.utcfromtimestamp(i['date']).strftime('%Y-%m-%d')
    if date in listDate:
        index = listDate.index(date)
        listLikes[index] += i['likes']['count']
    else:
        listDate.append(date)
        listLikes.append(i['likes']['count'])
       
print('Дни активности: \n',listDate)
print('Количество лайков за каждый день: \n', listLikes)

writeInTxt(allLikes, listDate, listLikes)