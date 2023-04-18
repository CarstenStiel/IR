import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

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
def getEntriesToJSONL(input_File, output_File):
    # Öffne die Eingabe-JSONL-Datei und die Ausgabe-JSONL-Datei
    with open(input_File, "r") as input_file, open(output_File, "w") as output_file:
        # Iteriere über jede Zeile der Eingabe-JSONL-Datei
        for line in input_file:
            # Lade die JSON-Daten aus der Zeile
            data = json.loads(line)

            # Extrahiere nur die "doc_id" und "text" Felder
            filtered_data = {"doc_id": data["id"], "text": str(data)}

            # Schreibe die extrahierten Daten als JSON in die Ausgabe-JSONL-Datei
            output_file.write(json.dumps(filtered_data) + "\n")


def setXML(file_path, file_name):
    if checkForXML(file_path, file_name) == False:
        try:
            root = ET.Element("topics")
            tree = ET.ElementTree(root)
            tree.write(file_path)
            print(f"Die Datei {file_name} wurde erstellt.")
        except Exception as e:
            print(f"Fehler beim Erstellen der Datei {file_name}: {e}")
    else:
        print("Die Datei existiert bereits.")
        overwrite = input('Soll die Datei überschrieben werden? ("Ja" oder "Nein"): ')
        while overwrite not in ["Ja", "Nein"]:
            overwrite = input('Falsche Eingabe! Soll die Datei überschrieben werden? ("Ja" oder "Nein"): ')

        if overwrite == "Ja":
            root = ET.Element("topics")
            tree = ET.ElementTree(root)
            tree.write(file_path)
            print(f"Die Datei {file_name} wurde überschrieben.")
        else:
            tree = ET.parse(file_path)
            root = tree.getroot()
            print(f"Es befinden sich {len(root)} Topics in der Datei.")

    topics = -1
    confirmation = "Nein"
    while (confirmation != "Ja"):
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

"""
Prüft, ob eine XML-Datei mit dem gegebenen Namen im gegebenen Verzeichnis vorhanden ist.
Wenn die Datei nicht vorhanden ist, wird eine neue Datei mit dem gegebenen Namen im gegebenen Verzeichnis erstellt.
"""
def checkForXML(file_path, file_name):
    if os.path.isfile(file_path):
        print(f"Die Datei {file_name} existiert bereits.")
        return True
    else:
        print(f"Die Datei {file_name} existiert nicht.")
        return False


#Überprüft, ob eine Datei im gegeben Pfad enthalten ist und erstellt ggf. eine
def checkForFile(File_Path, File_Name):
    # Überprüfe, ob die JSONL-Datei bereits vorhanden ist
    if os.path.isfile(os.path.join(File_Path)):

        print("Die Datei existiert bereits.\n")
    else:
        # Öffne die Ausgabe-JSONL-Datei zum Schreiben
        with open(File_Path, 'w') as f:
            f.write(json.dumps(""))
            print(f"Die Datei {File_Name} wurde in Folgendem Pfad erstellt: {File_Path}\n")