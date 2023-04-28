# DNC_Limited

## Project Structure

1. ***notebook:***
    - The Jupyter Notebook is located here, named [DNC_Limited_Data.ipynb](notebook/DNC_Limited_Data.ipynb)
    - The data, that we need are located inside the folder [data](notebook/data)
2. ***notebook/data:***
   - The following files are located here:
     * [ir-anthology-final](notebook/data/ir-anthology-07-11-2021-ss23.jsonl): Created document collection in the JSONL format, with "doc_id" and "text" fields.
     * [topics](notebook/data/topics.xml): Topics in the XML format for Tira.
     * [ir-anthology-07-11-2021-ss23](notebook/data/ir-anthology-07-11-2021-ss23.jsonl): File that is given to extract the needed information.
3. ***testingCode:***
   - The code used for testing in the respective IDE before being used in the Jupyter Notebook is located here.

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
Navigate in the terminal to the [notebook](notebook/) directory of the project and enter the following command:
```
jupyter notebook
```
Select the [DNC_Limited_Data.ipynb](notebook/DNC_Limited_Notebook.ipynb) file in the Jupyter Notebook interface to start the notebook.

## Commands good to know
The following commands are used for Windows Powershell
1. ***Docker:***
    - docker build image with [iranthology-DNC_Limited.py](notebook/iranthology-DNC_Limited.py) (use this command inside the [notebook](notebook/)):
        ```
        docker build -t dnc-limited-ir-dataset -f Dockerfile.iranthology .
        ```
    - delete everything (images and containers):
        ```
        docker system prune -a
        ```
    - docker compose:
        ```
        docker compose up
        ```

2. ***Tira:***
    - Tira run (use this command inside the [notebook](notebook/)):
    ```
    tira-run --output-directory ${PWD}/dnc-limited-dataset-tira --image dnc-limited-ir-dataset --allow-network true --command '/irds_cli.sh --ir_datasets_id iranthology-DNC_Limited --output_dataset_path $outputDir'
    ```