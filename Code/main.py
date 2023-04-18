import Data

# Pfade und Namen zur JSONL-Datein angeben
xml_File_name = "topics.xml"
input_File_Name = "ir-anthology-07-11-2021-ss23.jsonl"
output_File_Name = "ir-anthology-final.jsonl"
input_File_Path = 'C:/Users/timot/Desktop/InRet/' + input_File_Name
output_File_Path = 'C:/Users/timot/Desktop/InRet/' + output_File_Name
xml_File_Path = 'C:/Users/timot/Desktop/InRet/' + xml_File_name

if __name__ == '__main__':

    Data.checkForFile(output_File_Path, output_File_Name) #Überprüft, ob eine JSONL Datei verhanden ist, und erstellt ggf. eine
    Data.getEntriesToJSONL(input_File_Path, output_File_Path) #
    print("Anzahl Entitäten: ", Data.countEntriesJSONL(output_File_Path))
    Data.setXML(xml_File_Path, xml_File_name)