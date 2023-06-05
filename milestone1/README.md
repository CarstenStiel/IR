# DNC_Limited

***The entire repository can be found at: [https://github.com/CarstenStiel/IR](https://github.com/CarstenStiel/IR)***

## "milestone1" structure

1. ***data:***
   - The following files are located here:
     * [dnc-limited-documents.jsonl](milestone1/data/dnc-limited-documents.jsonl): Created document collection in the JSONL format, with "doc_id" and "text" fields.
     * [dnc-limited-topics.xml](milestone1/data/dnc-limited-topics.xml): Topics in the XML format for Tira.
     * [ir-anthology-07-11-2021-ss23](milestone1/data/ir-anthology-07-11-2021-ss23.jsonl): File that is given to extract the needed information.
     * [qrels.txt](milestone1/data/qrels.txt): Sorted qrels as txt file.
2. ***[.gitignore](.gitignore):*** Dependencies, that should be ignored for git(not relevant).
3. ***[dnc-limited-notebook-milestone1.ipynb](dnc-limited-notebook-milestone1.ipynb):*** Notebook for "milestone1" one with code documentation and reflection.
4. ***[Dockerfile](Dockerfile):*** Dockerfile to build the needed "milestone1" image.
5. ***[iranthology-dnc-limited.py](iranthology-dnc-limited.py):*** Pythonfile for tira for "formats"
6. ***[Pipfile](Pipfile) and [Pipfile.lock](Pipfile.lock):*** Files for your jupyter notebook for execution (not relevant).

## Step-by-Step guide

Please follow these steps to create the needed output:

- Navigate in your terminal to the "milestone1" folder
- Open "Docker Desktop"

### Docker

- Build the image for "milestone1":
    ```
    docker build -t milestone1 .
    ```
- (optional) Run the docker image:
    ```
    docker run -p 8888:8888 --rm -ti -w /workspace -v ${PWD}:/workspace --entrypoint jupyter milestone1 notebook --allow-root --ip 0.0.0.0
    ```

### Tira

1. Import data:
    ```
    tira-run --output-directory ${PWD}/iranthology-dataset-tira --image milestone1 --allow-network true --command '/irds_cli.sh --ir_datasets_id iranthology-dnc-limited --output_dataset_path $outputDir'
    ```
2. Retrieve data:
     ```
     tira-run --input-directory ${PWD}/iranthology-dataset-tira --image webis/tira-ir-starter-pyterrier:0.0.2-base --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/full-rank-pipeline.ipynb'
     ```
3. Render the retrieval results:
    ```
    tira-run --input-directory ${PWD}/tira-output --image milestone1 --allow-network true --command 'diffir --dataset iranthology-dnc-limited --web $outputDir/run.txt > $outputDir/run.html'
    ```