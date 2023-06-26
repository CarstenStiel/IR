docker stop $(docker ps -a -q)
docker build -t milestone3 .
docker run -d -p 8888:8888 --rm -ti -v ${PWD}:/workspace --entrypoint jupyter milestone3  notebook --allow-root --ip 0.0.0.0
 tira-run --input-directory ${PWD}/iranthology-dataset-tira --output-directory ${PWD}/bm25-multi-field-output --image milestone3 --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/dnc-limited-notebook-bm25-multi-field.ipynb'
tira-run --output-directory ${PWD}/bm25-multi-field-output --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-dnc-limited/ir-datasets:0.0.1 --allow-network true --command 'diffir --dataset iranthology-dnc-limited --web $outputDir/run.txt > $outputDir/run.html'
tira-run --input-directory ${PWD}/bm25-multi-field-output --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-dnc-limited/ir-datasets:0.0.1 --allow-network true --command 'ir_measures iranthology-dnc-limited $inputDataset/run.txt nDCG@10 MRR P@10 Recall@100'

