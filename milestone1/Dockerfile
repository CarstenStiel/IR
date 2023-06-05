# Use the official Jupyter image as the base image
FROM webis/tira-ir-datasets-starter:0.0.54

# Install any required packages
RUN apk add jq libffi-dev && pip3 install jupyter ir_datasets

# Copy the notebook and all necessary files into the container
COPY dnc-limited-notebook-milestone1.ipynb iranthology-dnc-limited.py data/dnc-limited-topics.xml  data/dnc-limited-documents.jsonl data/qrels.txt /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]