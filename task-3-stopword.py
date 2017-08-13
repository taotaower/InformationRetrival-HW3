import json
import io

with open('task2/1-gram.json', 'r') as f:
    data = json.load(f)

#print data
termFreq = {}
for d in data:
    freq = sum(data[d].values())
    termFreq[d] = freq
top100TermFreq = sorted(termFreq.iteritems(), key=lambda d: d[1], reverse=True)[0:200]

docFreq = {}

for d in data:
    docFreq[d] = len(data[d])
    top100DocFreq = sorted(docFreq.iteritems(), key=lambda d: d[1], reverse=True)[0:200]


top100TermsTF = [t[0] for t in top100TermFreq]
top100TermsDF = [t[0] for t in top100DocFreq]

stopList = set([val for val in top100TermsTF if val in top100TermsDF][0:100] + top100TermsDF[0:10])

line ='\n'.join(list(stopList))

fobj = io.open('stoplist.txt', 'a', encoding='utf8')
fobj.write(line)
fobj.close()
