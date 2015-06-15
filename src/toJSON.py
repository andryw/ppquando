__author__ = 'andryw'
import codecs

programacao = codecs.open('tudo.csv', encoding='utf-8-sig')

documentos = {}

import json
import operator

def saveTags(tagsDict):
    jsonTags = []
    tags_sorted = sorted(tagsDict.items(), key=operator.itemgetter(1),reverse = True)
    for tag in tags_sorted:
        jsonTags.append({'tag':tag[0],'count':tag[1]})
    tagsJson = codecs.open('tags.json', "w",encoding='utf-8-sig')
    json.dump(jsonTags,tagsJson, encoding='utf-8-sig')

def addTag(tagsDict,tag):
    if not (tag in tagsDict):
        tagsDict[tag] = 0
    tagsDict[tag] += 1

tags = set()
tagsDict = {}
i = 0

for line in programacao.readlines():

    if line:
        i = i + 1

        if i == 1:
            continue
        temp = line.replace("\n","").split(",")
        print temp
        data = temp[0]
        banda = temp[1]
        tag = temp[2]
        value = temp[3]

        if (not documentos.has_key(data)):
            documentos[data] = {}
        if (not documentos[data].has_key(banda)):
            documentos[data][banda] = {}
        if (tag != 'NA'):
            documentos[data][banda][tag] = value
            tags.add(tag)
            addTag(tagsDict,tag)

saveTags(tagsDict)
tudoJson = codecs.open('tudo.json', "w",encoding='utf-8-sig')
json.dump(documentos,tudoJson, encoding='utf-8-sig')