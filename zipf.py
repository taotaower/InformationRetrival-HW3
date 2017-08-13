from __future__ import division
from pylab import *
from collections import Counter
import json

with open('task2/1-gram.json', 'r') as f:
    data = json.load(f)

#with open('task2/2-gram.json', 'r') as f:
#    data = json.load(f)

#with open('task2/3-gram.json', 'r') as f:
#    data = json.load(f)


termFreq = {}
for d in data:
    freq = sum(data[d].values())
    termFreq[d] = freq


tokens_with_count = Counter(termFreq)
counts = array(tokens_with_count.values())
tokens = tokens_with_count.keys()

# A Zipf plot
ranks = arange(1, len(counts)+1)

indices = argsort(-counts)
frequencies = counts[indices]
#print len(ranks)

loglog(ranks, frequencies, marker=".")
title("Zipf plot for 1-gram ")
#title("Zipf plot for 2-gram ")
#title("Zipf plot for 3-gram ")
xlabel("Frequency rank of token")
ylabel("Absolute frequency of token")
grid(True)

show()
