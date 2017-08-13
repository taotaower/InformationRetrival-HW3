#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json



def readFolder(rootDir): # read the docs in the folder
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        return files



def getIndex(folder, n):
    words = {}
    totalTokens = {}
    files = readFolder(folder)
    files.pop(0)
    for f in files:
        u = re.match(r'(.*?)(.txt)', f)
        docID = u.group(1)
        path = folder + '/' + f
        f = open(path, 'r')
        content = f.read()
        f.close()
        nGrams = getNGrams(content.split(), n)
        totalTokens[docID] = len(nGrams)
        for g in nGrams:
            if words.has_key(g):
                if words[g].has_key(docID):
                    words[g][docID] += 1
                else:
                    words[g][docID] = 1
            else:
                words.update({g: {docID: 1}})
    nameOfIndex = str(n) + '-gram'
    nameOfTotalTokens = str(n) + '-totalTokens'
    outputDict(words, nameOfIndex)
    outputDict(totalTokens, nameOfTotalTokens)


def outputDict(dic,name):
    fileName = 'task2/' + name + '.json'
    with open(fileName, 'w') as f:
        json.dump(dic, f)


def getNGrams(wordlist, n):
    nGrams =  [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]
    return [' '.join(nGram) for nGram in nGrams]


getIndex('cleanedDocs', 1)
getIndex('cleanedDocs', 2)
getIndex('cleanedDocs', 3)