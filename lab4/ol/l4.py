# coding: utf-8
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import os
import shutil
import re

from requests.api import request

def getSections(url):
    page = requests.get(url)
    if (page.status_code == 200):
        page.encoding = urlEncoding
        soup = BeautifulSoup(page.text, "html.parser")

        comments = soup.findAll(text=lambda t: isinstance(t, Comment))
        comments += soup.select('[style*="display:none"]')

        for comment in comments:
            comment.extract()

        sections = soup.findAll(class_='tema')
        return sections
    else:
        raise ConnectionError('Соединение не было успешно установлено')

def getSection(sections):
    sectionsTitles = []
    print('Выберите раздел: ')
    i = 1
    for item in sections:
        sectionsTitles.append(item.text)
        print(f'{i}) {item.text}')
        i += 1

    theme = int(input())

    if (theme >= 1 and theme <= len(sectionsTitles)):
        print(f"Выбран раздел \"{sectionsTitles[theme - 1]}\"")
    else:
        print("Неверный раздел")

    sectionUrl = url + sections[theme - 1].get('href')
    print(f'Ссылка раздела: {sectionUrl}')

    return (sectionUrl, sectionsTitles[theme - 1])

def getArticles(sectionUrl):
    sectionRequest = requests.get(sectionUrl)
    sectionRequest.encoding = urlEncoding
    selectedSectionSoup = BeautifulSoup(sectionRequest.text, 'html.parser')

    pagesQuantity = int(selectedSectionSoup.findAll(class_='page')[-1].text)
    print(f'Количество страниц: {pagesQuantity}')

    userChoice = int(input('Сколько страниц парсим? (-1 для выбора всех возможных)\n'))
    if userChoice >= 0:
        pagesToParse = min(pagesQuantity, userChoice)

    userChoice = int(input('С какой страницы парсим?\n'))

    if userChoice >=0:
        currentPage = min(userChoice, pagesQuantity)
    else:
        currentPage = 1

    lastPage = currentPage + pagesToParse
    pages = []
    while (currentPage < lastPage):
        page = requests.get(f'{sectionUrl}', params={'p': currentPage})
        page.encoding = urlEncoding
        if (page.status_code == 200):
            currentSoup = BeautifulSoup(page.text, 'html.parser')
            pages.append(currentSoup)
        currentPage += 1

    articleSoups = []
    articleUrls = []
    articlePages = []

    for page in pages:
        articleUrls += map(lambda elem: elem.get('href'), page.findAll('a', class_='announce'))

    for articleUrl in articleUrls:
        url = f'https://krasotka.biz{articleUrl}'
        page = requests.get(url)
        page.encoding = urlEncoding

        if (page.status_code == 200):
            print(f'{url} found')
            articlePages.append(page)
        else:
            print(f'{url} connection error')

    for articlePage in articlePages:
        soup = BeautifulSoup(articlePage.text, 'html.parser')
        articleSoups.append(soup.find('table').find_all('td')[1])

    return articleSoups

def makedir(path):
    try:
        os.mkdir(path)
    except Exception:
        shutil.rmtree(path)
        os.mkdir(path)

def parse(articleSoups):
    for soup in articleSoups:
        noindex = soup.select('noindex')
        for noindexSection in noindex:
            noindexSection.extract()

        textSoups = soup.select('h1,p:not(.aname)')

        for textSoup in textSoups:
            article = textSoup.text.replace(':', '.').replace('/', '.').replace('"', '.').replace('?', '.').replace('\\', '.').replace(':', '.')[:64].strip()
            if article != '':
                articleName = article
                break

        makedir(f'{theme}/{articleName}')
        filename = f'{theme}/{articleName}/{articleName}.txt'
        file = open(filename, 'w', encoding = 'utf-8')


        print(filename)
        for article in textSoups:
            textToWrite = article.text + '\n\n' if article.text != '' else ''
            file.write(textToWrite)
        file.close()

        images = soup.select('img')
        
        for img in images:
            imagePath = img['src']
            startUrl = imagePath.find('/')
            link = f'{url}{imagePath[startUrl:]}'
            if re.search(r'(png|jpg|jpeg)', link):
                print(link)
                f = open(f'{theme}/{articleName}/{os.path.basename(link)}', 'wb')
                f.write(requests.get(link).content)
                f.close()

url = 'https://www.krasotka.biz'
urlEncoding = 'cp1251'

print('Парсим', url)
    
try:
    sections = getSections(url)
    (sectionUrl, theme) = getSection(sections)
    makedir(theme)
    articleSoups = getArticles(sectionUrl)
    parse(articleSoups)

except Exception as e:
    print('Unexpected error')
    print(e)
