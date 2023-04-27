import json
import os
import xml.etree.ElementTree as ET

#
def getDirectory():
    current_directory = os.getcwd()
    current_directory = os.path.dirname(current_directory)
    if current_directory.__contains__("TestingCode"):
        current_directory = os.path.dirname(current_directory)
    current_directory = os.path.join(current_directory, "notebook\\")
    return current_directory

#Zählt die Einträge einer JSONL Datei
def countEntriesJSONL(input_File):
    # Zähler für Einträge initialisieren
    count = 0

    # JSONL-Datei öffnen und Einträge zählen
    with open(input_File, 'r') as f:
        for line in f:
            # Eintrag(Zeile) zählen
            count += 1

    # Ergebnis zurückgeben
    return count


#Schreibt gewünschte Einträge ("doc_id" und "text") von einer JSONL in eine andere
def getEntriesToJSONL(inputFile, outputFilePath, outputFileName):
    count = 0

    if not checkForFile(outputFilePath,outputFileName):
        with open(outputFilePath, 'w') as f:
            try:
                f.write("")
                print(f"Die Datei {outputFileName} wurde in folgendem Pfad erstellt: {outputFilePath}")
            except Exception as e:
                print(f"Fehler beim Erstellen der Datei {outputFileName}: {e}")

    # Öffne die Eingabe-JSONL-Datei und die Ausgabe-JSONL-Datei
    with open(inputFile, "r") as input_file, open(outputFilePath, "w") as output_file:
        # Iteriere über jede Zeile der Eingabe-JSONL-Datei
        for line in input_file:
            if count < 5:
                # Lade die JSON-Daten aus der Zeile
                lineJSON = json.loads(line)
                array = []
                for key in lineJSON:
                    array.append(lineJSON[key])
                stringJSON = " ".join(str(item) for item in array)

                # Extrahiere nur die "doc_id" und "text" Felder
                filtered_data = {"doc_id": lineJSON["id"], "text": stringJSON}

                # Schreibe die extrahierten Daten als JSON in die Ausgabe-JSONL-Datei
                output_file.write(json.dumps(filtered_data) + "\n")
                count += 1


def setXML(file_path, file_name):
    overwrite = 0
    if checkForFile(file_path, file_name) == False:
        try:
            root = ET.Element("topics")
            tree = ET.ElementTree(root)
            tree.write(file_path)
            print(f"Die Datei {file_name} wurde erstellt.")
        except Exception as e:
            print(f"Fehler beim Erstellen der Datei {file_name}: {e}")
    else:
        overwrite = input('Soll die Datei überschrieben werden [1] oder etwas angehangen werden [2]? (Wähle 1, 2 oder Exit):')
        while overwrite not in ["1", "2", "Exit"]:
            overwrite = input('Falsche Eingabe! Soll die Datei überschrieben werden? (Wähle 1, 2 oder Exit):')

        if overwrite == "1":
            root = ET.Element("topics")
            tree = ET.ElementTree(root)
            tree.write(file_path)
        elif overwrite == "2":
            tree = ET.parse(file_path)
            root = tree.getroot()
            print(f"Es befinden sich {len(root)} Topics in der Datei.")
        else:
            return

    topics = -1
    confirmation = "Nein"
    while confirmation != "Ja":
        if overwrite == "2":
            topics = input("Anzahl der neuen Topics:")
            print(f"Die Anzahl der neuen Topics soll {topics} betragen.")
        else:
            topics = input("Anzahl der Topics:")
            print(f"Die Anzahl der Topics soll {topics} betragen.")
        confirmation = input("Ist dies korrekt? (Ja/Nein):")

    for i in range(int(topics)):
        new_topic = ET.SubElement(root, "topic", number="")
        new_title = ET.SubElement(new_topic, "title")
        new_title.text = "  "
        new_description = ET.SubElement(new_topic, "description")
        new_description.text = "  "
        new_narrative = ET.SubElement(new_topic, "narrative")
        new_narrative.text = "  "

    ET.indent(tree, '  ') #Richtige Einrückung für die Datei
    tree.write(file_path) #Schreibt in die Datei

    if overwrite == "1":
        print(f"Die Datei {file_name} wurde überschrieben und enthält nun {len(root)} Topics.")
    else:
        print(f"Es befinden sich nun {len(root)} Topics in {file_name}.")


"""
Prüft, ob eine XML-Datei mit dem gegebenen Namen im gegebenen Verzeichnis vorhanden ist.
Wenn die Datei nicht vorhanden ist, wird eine neue Datei mit dem gegebenen Namen im gegebenen Verzeichnis erstellt.
"""
def checkForFile(file_path, file_name):
    if os.path.isfile(file_path):
        print(f"Die Datei {file_name} existiert bereits.")
        return True
    else:
        print(f"Die Datei {file_name} existiert nicht.")
        return False