import json
import os

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


def get_5Elements(file_path):
    # Öffne die Datei und lese sie zeilenweise ein
    with open(file_path, "r") as f:
        # Lese die ersten fünf Zeilen
        for i, line in enumerate(f):
            if i >= 5:
                break
            # Lade das JSON-Objekt aus der Zeile
            obj = json.loads(line)
            # Gib das Objekt aus
            for key, value in obj.items():
                print(key, ":", value, ",")


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