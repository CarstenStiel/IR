import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset

DATASET_URL = 'https://raw.githubusercontent.com/CarstenStiel/IR/main/notebook/CreatedData'

class PangramDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text

ir_datasets.registry.register('pangrams', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'ir-anthology-final.jsonl')], expected_md5='3f67adc5d99a7b6b7a410d4aefc8fe3b'), doc_cls=PangramDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'topics.xml')], expected_md5='411647769eabf8dbcaac85cdb734c50d'), lang='en'),
))