from pep_parse.CONSTANTS import BASE_DIR, STATUSES_FILENAME
from pep_parse.items import PepParseItem


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_counter = dict()

    def process_item(self, item: PepParseItem, spider):
        if item['status'] not in self.pep_counter.keys():
            self.pep_counter[item['status']] = 1
        else:
            self.pep_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
                f'{BASE_DIR}/{STATUSES_FILENAME}',
                mode='w',
                encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            total_counter = 0
            for status, count in self.pep_counter.items():
                total_counter += count
                f.write(f'{status},{count}\n')
            f.write(f'Total,{total_counter}\n')
