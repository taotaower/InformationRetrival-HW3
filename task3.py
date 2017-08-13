#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from prettytable import PrettyTable
import io


def buildTermFreqTab(data,outputName):
    termFreq = {}
    for d in data:
        freq = sum(data[d].values())
        termFreq[d] = freq
    sortedTermFreq = sorted(termFreq.iteritems(), key=lambda d: d[1], reverse=True)

    t = PrettyTable(['NO.', 'term', 'frequency'])
    n = 1
    for row in sortedTermFreq:
        row = list(row)
        row.insert(0, n)
        t.add_row(row)
        n += 1

    fileName = outputName + '.txt'
    fobj = open(fileName, 'w')
    fobj.write(str(t))
    fobj.close()


with open('task2/1-gram.json', 'r') as f:
    data1 = json.load(f)

buildTermFreqTab(data1, '1-gram-termFreq')

with open('task2/2-gram.json', 'r') as f:
    data2 = json.load(f)

buildTermFreqTab(data2, '2-gram-termFreq')

with open('task2/3-gram.json', 'r') as f:
    data3 = json.load(f)

buildTermFreqTab(data3, '3-gram-termFreq')


def buildDocFreqTab(data,outputName):
    sortedDocFreq = sorted(data.iteritems(), key=lambda d: d[0], reverse=False)
    for index in sortedDocFreq:
        docIDs = index[1].keys()
        docFreq = len(docIDs)  # int
        docs = ",".join(docIDs)  # str
        lines = 'term:' + index[0] + '##docs:' + '[' + docs + ']' + '##frequency:' + str(docFreq) + '\n'
        fobj = io.open(outputName, 'a', encoding='utf8')
        fobj.write(lines)
        fobj.close()


with open('task2/1-gram.json', 'r') as f:
    data1 = json.load(f)

buildDocFreqTab(data1, '1-gram-df')

with open('task2/2-gram.json', 'r') as f:
    data2 = json.load(f)

buildDocFreqTab(data2, '2-gram-df')

with open('task2/3-gram.json', 'r') as f:
    data3 = json.load(f)

buildDocFreqTab(data3, '3-gram-df')