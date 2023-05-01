import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset

DATASET_URL = 'https://raw.githubusercontent.com/CarstenStiel/IR/main/notebook/data/'


class DNCDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text


ir_datasets.registry.register('iranthology-dnc-limited', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'dnc-limited-documents.jsonl')], expected_md5='c434caa3b4a2a37d6685c3b6c2c4b012'), doc_cls=DNCDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'dnc-limited-topics.xml')], expected_md5='93458db12a666b8b1166d39446d0d759'), lang='en')
))