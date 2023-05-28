# DNC_Limited Milestone 2

***The entire repository can be found at: [https://github.com/CarstenStiel/IR](https://github.com/CarstenStiel/IR)***

## Structure

1. ***[.gitignore](.gitignore):*** Dependencies, that should be ignored for git(not relevant).
2. ***[dnc-limited-notebool-milestone2.ipynb](dnc-limited-notebook-milestone2.ipynb):*** Notebook for "milestone1" one with code documentation and reflection.
3. ***[Dockerfile](Dockerfile):*** Dockerfile to build the needed "milestone2" image.
4. ***[Pipfile](Pipfile) and [Pipfile.lock](Pipfile.lock):*** Files for your jupyter notebook for execution (not relevant).

## Step-by-Step guide

The following Code is for the use inside the "pyterrier" Docker image and couldn´t function, if you want to execute it in your notebook!

Please follow these steps to create the needed output:

### Pre-condition

1. Navigate in your terminal to the "milestone2" folder and open "Docker Desktop"

2. Pull the image of the "milestone1" with the qrels command
    ```
    docker pull carstenstiel/milestone1
    ```
3. Execute the tira-run command for the "milestone1" to get the needed output:
    ```
    tira-run --output-directory ${PWD}/iranthology-dataset-tira --image carstenstiel/milestone1 --allow-network true --command '/irds_cli.sh --ir_datasets_id iranthology-dnc-limited --output_dataset_path $outputDir'
    ```
   
### Milestone 2

4. Build an image for the current milestone:
    ```
    docker build -t milestone2 .
    ```
5. Run this image:
    ```
    docker run -p 8888:8888 --rm -ti -v ${PWD}:/workspace --entrypoint jupyter milestone2  notebook --allow-root --ip 0.0.0.0
    ```
6. Execute this notebook as tira would do:
    ```
    tira-run --input-directory ${PWD}/iranthology-dataset-tira --output-directory ${PWD}/bm25-output --image milestone2 --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/dnc-limited-notebook-milestone2.ipynb'
    ```
7. Render results:
    ```
    tira-run --output-directory ${PWD}/bm25-output --image carstenstiel/milestone1 --allow-network true --command 'diffir --dataset iranthology-dnc-limited --web $outputDir/run.txt > $outputDir/run.html'
    ```
8. Evaluate the effectiveness of the baseline on your relevance judgments:
    ```
    tira-run --input-directory ${PWD}/bm25-output --image carstenstiel/milestone1 --allow-network true --command 'ir_measures iranthology-dnc-limited $inputDataset/run.txt nDCG@10 MRR P@10 Recall@100'
    ```