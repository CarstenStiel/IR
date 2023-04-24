# DNC_Limited

## Aufbau des Projektes

1. ***Jupyter Notebook:***
    - Das Jupyter Notebook befindet hier im übergeordnetem Verzeichnis unter dem Namen [DNC_Limited_Data.ipynb](DNC_Limited_Data.ipynb)
2. ***CreatedData:***
   - Hier befinden sich folgende Datein:
     * [ir-anthology-final](CreatedData/ir-anthology-final.jsonl): Erstellte Dokumentensammlung im Format "doc_id" und "text" im JSONL-Format
     * [topics](CreatedData/topics.xml): Topics im XML-Format für Tira
3. ***Code:***
   - Hier befindet sich der Code, der zum Testen in der jeweiligen IDE genutzt wird, bevor er im Jupyter Notebook verwendet wird.

## Installationen

Für den ersten Start des Projektes sollte folgendes installiert sein:

***Wichtig:*** Hier findest du die Anforderungen mit einer Installationsanleitung für Windows. Beachte, dass das Terminal als <ins>Administrator</ins> ausgeführt werden sollte!
1. ***Python:***
   - Lade "Python" von folgender Website herunter und führe die angegebenen Schritte aus: https://www.python.org/downloads/
3. ***Pipenv:***
   - Führe folgenden Befehl im Terminal aus:
     ```
     pip install pipenv
     ```
3. ***Jupyter:***
   - Führe folgenden Befehl im Terminal aus:
      ```
      pip install jupyter
      ```
4. ***Docker:***
   - Lade "Docker Desktop" von folgender Website herunter und führe die angegebenen Schritte aus: https://docs.docker.com/get-docker/
   - ***Beachte:*** Lies dir für eine reibungslose installation alles genau durch (WSL2, etc.)!
5. ***Python IDE:***
   - <ins>Persönliche</ins> Empfehlung liegt hier auf PyCharm unter: https://www.jetbrains.com/pycharm/download/#section=windows 
     
## Starten des Jupyter Notebooks
Navigiere im Terminal zum übergeordnetem Verzeichnis des Projektes und gebe folgenden Befehl ein:
```
jupyter notebook
```
Wähle die [DNC_Limited_Data.ipynb](DNC_Limited_Data.ipynb) Datei in der Jupyter Notebook-Oberfläche um das Notebook zu starten