import csv

from pep_parse.CONSTANTS import BASE_DIR, STATUSES_FILENAME
from pep_parse.items import PepParseItem


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_counter = dict()

    def process_item(self, item: PepParseItem, spider):
        self.pep_counter[
            item['status']
        ] = self.pep_counter.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        with open(
                f'{BASE_DIR}/{STATUSES_FILENAME}',
                mode='w',
                encoding='utf-8',
                newline=''
        ) as f:
            writer = csv.writer(f)
            total_counter = 0
            output_rows = [['Статус', 'Количество'], ]
            for status, count in self.pep_counter.items():
                total_counter += count
                output_rows.append([status, count])
            output_rows.append(['Total', total_counter])
            writer.writerows(output_rows)
