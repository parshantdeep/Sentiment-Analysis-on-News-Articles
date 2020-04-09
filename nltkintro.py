##NLTK
rawdata = open("SMSSpamCollection.tsv").read()

parsedData = rawdata.replace('\t','\n').split('\n')
print(parsedData)
labelList = parsedData[0::2]
textList = parsedData[1::2]
print(labelList)
print(textList)