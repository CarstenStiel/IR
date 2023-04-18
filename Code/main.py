import Data

# Pfade und Namen zur JSONL-Datein angeben
xmlFileName = "topics.xml"
inputFileName = "ir-anthology-07-11-2021-ss23.jsonl"
outputFileName = "ir-anthology-final.jsonl"
inputFilePath = 'C:/Users/timot/Desktop/InRet/' + inputFileName
outputFilePath = 'C:/Users/timot/Desktop/InRet/' + outputFileName
xmlFilePath = 'C:/Users/timot/Desktop/InRet/' + xmlFileName

if __name__ == '__main__':

    Data.getEntriesToJSONL(inputFilePath, outputFilePath, outputFileName)
    print(f"Anzahl Entitäten in {outputFileName}: ", Data.countEntriesJSONL(outputFilePath), "\n")
    Data.setXML(xmlFilePath, xmlFileName)