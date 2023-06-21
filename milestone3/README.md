# DNC_Limited Milestone 3

***The entire repository can be found at: [https://github.com/CarstenStiel/IR](https://github.com/CarstenStiel/IR)***

## Structure

1. ***[.gitignore](.gitignore):*** Dependencies, that should be ignored for git(not relevant).
2. ***[dnc-limited-notebool-milestone2.ipynb](dnc-limited-notebook-bm25.ipynb):*** Notebook for "milestone1" one with code documentation and reflection.
3. ***[Dockerfile](Dockerfile):*** Dockerfile to build the needed "milestone2" image.
4. ***[Pipfile](Pipfile) and [Pipfile.lock](Pipfile.lock):*** Files for your jupyter notebook for execution (not relevant).

## Step-by-Step guide

The following Code is for the use inside the "pyterrier" Docker image and couldn´t function, if you want to execute it in your notebook!

Please follow these steps to create the needed output:

### Pre-condition

1. Navigate in your terminal to the "milestone2" folder and open "Docker Desktop"

2. Pull the image of the "milestone1" with the qrels command
    ```
    docker pull registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-dnc-limited/ir-datasets:0.0.1
    ```
3. Execute the tira-run command for the "milestone1" to get the needed output:
    ```
    tira-run --output-directory ${PWD}/iranthology-dataset-tira --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-dnc-limited/ir-datasets:0.0.1 --allow-network true --command '/irds_cli.sh --ir_datasets_id iranthology-dnc-limited --output_dataset_path $outputDir'
    ```
   
### Milestone 2


4. Execute all steps in the respective notebook (precondition only needs to be executed once, as well as building the Docker image for milestone 3)