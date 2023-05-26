# DNC_Limited

***The entire repository can be found at: [https://github.com/CarstenStiel/IR](https://github.com/CarstenStiel/IR)***

## Notebook structure

1. ***notebook:***
    - The Jupyter Notebook is located here, named [dnc-limited-notebook.ipynb](dnc-limited-notebook.ipynb)
    - The data, that we need are located inside the folder [data](data)
2. ***data:***
   - The following files are located here:
     * [dnc-limited-documents.jsonl](data/dnc-limited-documents.jsonl): Created document collection in the JSONL format, with "doc_id" and "text" fields.
     * [dnc-limited-topics.xml](data/dnc-limited-topics.xml): Topics in the XML format for Tira.
     * [ir-anthology-07-11-2021-ss23](data/ir-anthology-07-11-2021-ss23.jsonl): File that is given to extract the needed information.

## Installations

The following should be installed for the first start of the project:

***Important:*** Here are the requirements with installation instructions for Windows. Note that the terminal should be run as <ins>administrator</ins>!
1. ***Python:***
   - Download "Python" from the following website and follow the instructions: https://www.python.org/downloads/
2. ***Pipenv:***
   - Run the following command in the terminal:
     ```
     pip install pipenv
     ```
3. ***Tira:***:
   - Run the following command in the terminal:
     ```
     pip3 install tira
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

## Starting the Jupyter Notebook
Enter the following command:
```
jupyter notebook
```
Select the [dnc-limited-notebook.ipynb](dnc-limited-notebook.ipynb) file in the Jupyter Notebook interface to start the notebook.

## Commands good to know
The following commands are used for Windows Powershell
1. ***Docker:***
    - delete everything (images and containers):
        ```
        docker system prune -a
        ```