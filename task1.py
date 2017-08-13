#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import io
from bs4 import BeautifulSoup
from py2casefold import casefold

def readFolder(rootDir): # read the docs in the folder
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        return files



def cleaner(folder,outputFolder):
    files = readFolder(folder)
    files.pop(0)
    for f in files:
        path = folder + '/' + f
        title,content = parser(path) # call parser to get the title and the contents of the article
        print title
        newPath = outputFolder + '/' + title + '.txt'
        #----- write the cleaned content into the aim file
       # print content
        fobj = io.open(newPath, 'w', encoding='utf8')
        fobj.write(content)
        fobj.close()


def parser(path):
    soup = BeautifulSoup(open(path),'lxml',from_encoding="utf-8")
    rawTitle = soup.title.string
    u = re.match(r'(.*?)(- Wikipedia)', rawTitle)
    title = u.group(1).replace(' ', '')

    #------------------clean the content of HTML
    guides = soup.find_all("div", id="siteSub") + soup.find_all("div", id="contentSub") + soup.find_all("div", id="jump-to-nav") + \
             soup.find_all("div", class_="hatnote") + soup.find_all("div", class_="printfooter")
    for g in guides:
        g.extract()
    tags = soup.find_all(href=re.compile("#cite_"))
    for t in tags:
        t.extract()
    scripts = soup.find_all('script')
    for s in scripts:
        s.extract()
    sides = soup.find_all("tr") + soup.find_all("dl")
    for s in sides:
        s.extract()
    heads = soup.find_all('h1') + soup.find_all('h2') + soup.find_all('h3') + soup.find_all('h4') + soup.find_all('h5')
    for h in heads:
        h.extract()
    references = soup.find("ol", class_="references")
    if references != None:
        references.extract()
    toc = soup.find("div", class_="toc")
    if toc != None:
        toc.extract()
    cates = soup.find_all("div", class_="catlinks")
    for c in cates:
        c.extract()
    lis = soup.find_all('li')
    for l in lis:
        l.extract()
    navigations = soup.find_all("div", id="mw-navigation") + soup.find_all("div", role="navigation") + soup.find_all(
        "div", class_="navigation")
    for n in navigations:
        n.extract()
    #-------------------end of cleaning the content of HTML

    s = casefold(soup.get_text()) # case folding
    loword = s.split() # get the list of words in the sentence
    level1 = [''.join(c for c in list(w) if c not in (
    '!', '(', ')', '<', '>', '{', '}', '[', ']', '?', ':', ';', '\"', '/', '\'', '\\', '|', '~', '`', '...')) for w in
              loword] # remove punctuation except ',' , '.' and '-'
    level2 = [removeEndPun(w) for w in level1] # remove the end punctuation ',' and '.' in the end of a word
    content = ' '.join(level2)
    return title ,content


def removeEndPun(word):  # remove the end punctuation ',' and '.' in the end of a word
    chars = list(word)
    chars.reverse()
    new = ''.join(chars)
    u = re.match(r'(\.|,|-?)(.*)', new)
    try:
        noEnd = u.group(2)
    except AttributeError:
        noEnd = u.group(1)
    cleaned = list(noEnd)
    cleaned.reverse()
    noPun = ''.join(cleaned)
    return noPun

cleaner('docs','cleanedDocs')