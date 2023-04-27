import Data

# Pfade und Namen zur JSONL-Datein angeben
xmlFileName = "topics.xml"
inputFileName = "ir-anthology-07-11-2021-ss23.jsonl"
outputFileName = "ir-anthology-final.jsonl"
inputFilePath = Data.getDirectory() + "data\\" + inputFileName
outputFilePath = Data.getDirectory() + "data\\" + outputFileName
xmlFilePath = Data.getDirectory() + "data\\" + xmlFileName

if __name__ == '__main__':

    print(outputFilePath)

    Data.getEntriesToJSONL(inputFilePath, outputFilePath, outputFileName)
    print(f"Anzahl Entitäten in {outputFileName}: ", Data.countEntriesJSONL(outputFilePath), "\n")