#DATASET_URL = 'https://raw.githubusercontent.com/tira-io/ir-experiment-platform/main/ir-datasets/tutorial/'

import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset

DATASET_URL = 'https://raw.githubusercontent.com/CarstenStiel/IR/main/notebook/data/'


class DNCDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text


ir_datasets.registry.register('iranthology-DNC_Limited', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'ir-anthology-final.jsonl')], expected_md5='81aada046fedd8915aee2d5ef2f6aae3'), doc_cls=DNCDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'topics.xml')], expected_md5='3cf876258c8db1c003d18804b4bce299'), lang='en')
))