import datetime
from pathlib import Path

DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parents[1]


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter_status = {}

    def process_item(self, item, spider):
        item['status'] = self.counter_status.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        with open(f'{BASE_DIR}/results/'
                  f'status_summary_'
                  f'{datetime.datetime.now().strftime(DT_FORMAT)}.csv',
                  mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, value in self.counter_status.items():
                f.write(f'{status}, {value}\n')
            f.write(f'Total,{sum(self.counter_status.values())}\n')
