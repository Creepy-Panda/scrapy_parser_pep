import csv
import collections
from pathlib import Path
from datetime import datetime as dt

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_status_dict = collections.defaultdict(int)
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.pep_status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
        file = BASE_DIR / 'results' / f'status_summary_{date}.csv'
        with open(file, 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['Статус', 'Количество'])
            w.writerows(self.pep_status_dict.items())
            w.writerow(['Total', sum(self.pep_status_dict.values())])
