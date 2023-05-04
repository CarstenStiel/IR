FROM webis/tira-ir-datasets-starter:0.0.54

RUN apk add jq libffi-dev && pip3 install jupyter

COPY iranthology-dnc-limited.py data/dnc-limited-documents.jsonl dnc-limited-notebook.ipynb data/dnc-limited-topics.xml /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]