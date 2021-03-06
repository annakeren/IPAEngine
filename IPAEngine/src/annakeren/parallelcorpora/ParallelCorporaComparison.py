'''
Created on 25 Mar 2016

@author: annakeren
'''
import re, urllib
from src.annakeren.wikiIPA.wikiIPA import Utils
from src.annakeren.ipa.persist import SqlitePersistence


def getAccumulatedCount(text, language1, language2):
    print language1 + "/" + language2
    allList = []
    selectPart1 = "select matches, resemblance from words where (ipa2='"
    selectPart2 = "' or ipa1='"
    selectPart3 = "') and ((language1='"
    selectPart4 = "' and language2='"
    selectPart5 = "') or (language1='"
    selectPart6 = "' and language2='"
    selectPart7 = "'));"
    words = text.split()
    connection = SqlitePersistence.SqlitePersistence.connect("//Users//annakeren//Documents//workspace//IPAEngine//IPAEngine//ipa.sqlite")
    cursor = connection.cursor()
    match = 0
    resemblance = 0.0
    wordsCountCompared = 0
    for word in words:
        wordStripped = word.strip()
        if len(wordStripped) > 1:
            if language2 == "Hebrew": 
                if wordStripped.startswith("ha"):
                    wordStripped = wordStripped[2:]
            selectStatement = selectPart1 + wordStripped + selectPart2 + wordStripped + selectPart3 + language1 + selectPart4 + language2 + selectPart5 + language2 + selectPart6 + language1 + selectPart7;
            cursor.execute(selectStatement)
            data = cursor.fetchone()
            if data is not None:
                match = match + data[0]
                resemblance = resemblance + data[1]
                wordsCountCompared = wordsCountCompared + 1
                print data[1]

    connection.close()
    allList.append(match)
    if wordsCountCompared != 0:
        resemblance = float(resemblance)/ float(wordsCountCompared)
    allList.append(str(resemblance))
    return allList

def getLanguage(fileName):
    language = ""
    mandarin = "Mandarin"
    german = "German"
    hebrew = "Hebrew"
    persian = "Persian"
    russian = "Russian"
    english = "English"
    if fileName.startswith(mandarin):
        language = mandarin
    if fileName.startswith(german):
        language = german
    if fileName.startswith(hebrew):
        language = hebrew
    if fileName.startswith(persian):
        language = persian
    if fileName.startswith(russian):
        language = russian
    if fileName.startswith(english):
        language = english
    return language
    
if __name__ == '__main__':
    files = Utils.Utils.readAllFilesFromFolder("/Users/annakeren/ParalleCorpra/")
    
    if len(files) != 3:
        
        texts =[[None]]*2
        languages = [[None]]*2
        i = 0
        for file in files:
            socket = urllib.urlopen(file)
            filePathSplit = re.split('/',file)
            filePathSplitLength = len(filePathSplit)
            fileName = filePathSplit[filePathSplitLength - 1]
            language = getLanguage(fileName)
            languages[i] = language
            texts[i] = socket.read()
            socket.close
            i = i + 1
        print languages[0] +" vs " + languages[1] + " Genesis"
        
        result1 = getAccumulatedCount(texts[0], languages[1], languages[0])
        print languages[1] +" compared to " + languages[0] + " absolute resemblance is " + str(result1[0]) + ", ratio is " + str(result1[1])
        
        result2 = getAccumulatedCount(texts[1], languages[0], languages[1])
        print languages[0] +" compared to " + languages[1] + " absolute resemblance is " + str(result2[0])+ ", ratio is  " + str(result2[1])
        
        
        
    else:
        print"Only two texts to compare should be in a folder"
