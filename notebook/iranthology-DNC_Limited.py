#DATASET_URL = 'https://raw.githubusercontent.com/tira-io/ir-experiment-platform/main/ir-datasets/tutorial/'

import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries, TrecQrels
from typing import NamedTuple, Dict
from ir_datasets.util.download import RequestsDownload
from ir_datasets.datasets.base import Dataset

DATASET_URL = 'https://raw.githubusercontent.com/CarstenStiel/IR/main/notebook/CreatedData/'


class PangramDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text


ir_datasets.registry.register('pangram', Dataset(
    JsonlDocs(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'ir-anthology-final.jsonl')], expected_md5='6fd25525cb321f6517c934f8ff8c96fb'), doc_cls=PangramDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.Download([RequestsDownload(DATASET_URL + 'topics.xml')], expected_md5='0916773cf11a1e3d7580268086f52cf4'), lang='en')
))