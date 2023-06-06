import datetime


DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
date_now = datetime.datetime.now()
BASE_DIR = f'{"results/"}'


result = {}


class PepParsePipeline:
    def open_spider(self, spider):
        ...

    def process_item(self, item, spider):
        if item['status'] in result:
            result[item['status']] += 1
        else:
            result[item['status']] = 1
        return item

    def close_spider(self, spider):
        with open(f'{BASE_DIR}/'
                  f'status_summary_{date_now.strftime(DT_FORMAT)}.csv',
                  mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, value in result.items():
                f.write(f'{status}, {value}\n')
            f.write(f'Total,{sum(result.values())}\n')
