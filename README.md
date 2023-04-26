# DNC_Limited

## English version

### Project Structure

1. ***Jupyter Notebook:***
    - The Jupyter Notebook is located here in the parent directory under the name [DNC_Limited_Data.ipynb](JupyterNotebook/DNC_Limited_Data.ipynb)
2. ***CreatedData:***
   - The following files are located here:
     * [ir-anthology-final](JupyterNotebook/CreatedData/ir-anthology-final.jsonl): Created document collection in the JSONL format, with "doc_id" and "text" fields.
     * [topics](JupyterNotebook/CreatedData/topics.xml): Topics in the XML format for Tira.
3. ***Code:***
   - The code used for testing in the respective IDE before being used in the Jupyter Notebook is located here.

### Installations

The following should be installed for the first start of the project:

***Important:*** Here are the requirements with installation instructions for Windows. Note that the terminal should be run as <ins>administrator</ins>!
1. ***Python:***
   - Download "Python" from the following website and follow the instructions: https://www.python.org/downloads/
3. ***Pipenv:***
   - Run the following command in the terminal:
     ```
     pip install pipenv
     ```
3. ***Jupyter:***
   - Run the following command in the terminal:
      ```
      pip install jupyter
      ```
4. ***Docker:***
   - Download "Docker Desktop" from the following website and follow the instructions: https://docs.docker.com/get-docker/
   - ***Note:*** Read everything carefully for a smooth installation (WSL2, etc.)!
5. ***Python IDE:***
   - <ins>Personal</ins> recommendation here is PyCharm at: https://www.jetbrains.com/pycharm/download/#section=windows 

### Starting the Jupyter Notebook
Navigate in the terminal to the parent directory of the project and enter the following command:
```
jupyter notebook
```
Select the [DNC_Limited_Data.ipynb](JupyterNotebook/DNC_Limited_Data.ipynb) file in the Jupyter Notebook interface to start the notebook.


## Deutsche Version

### Aufbau des Projektes

1. ***Jupyter Notebook:***
    - Das Jupyter Notebook befindet hier im übergeordnetem Verzeichnis unter dem Namen [DNC_Limited_Data.ipynb](JupyterNotebook/DNC_Limited_Data.ipynb)
2. ***CreatedData:***
   - Hier befinden sich folgende Datein:
     * [ir-anthology-final](JupyterNotebook/CreatedData/ir-anthology-final.jsonl): Erstellte Dokumentensammlung im Format "doc_id" und "text" im JSONL-Format
     * [topics](JupyterNotebook/CreatedData/topics.xml): Topics im XML-Format für Tira
3. ***Code:***
   - Hier befindet sich der Code, der zum Testen in der jeweiligen IDE genutzt wird, bevor er im Jupyter Notebook verwendet wird.

### Installationen

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
     
### Starten des Jupyter Notebooks
Navigiere im Terminal zum übergeordnetem Verzeichnis des Projektes und gebe folgenden Befehl ein:
```
jupyter notebook
```
Wähle die [DNC_Limited_Data.ipynb](JupyterNotebook/DNC_Limited_Data.ipynb) Datei in der Jupyter Notebook-Oberfläche um das Notebook zu starten