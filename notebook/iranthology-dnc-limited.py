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


ir_datasets.registry.register('iranthology-dnc-limited', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/dnc-limited-documents.jsonl'), doc_cls=DNCDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/dnc-limited-topics.xml'), lang='en')
))