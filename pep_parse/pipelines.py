import csv

from pep_parse.CONSTANTS import STATUSES_FILENAME


# filename = dt.datetime.now().strftime(FILENAME_FORMAT)


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        with open('temp_table.csv', encoding='utf-8', newline='') as File:
            reader = csv.reader(File, delimiter=',')
            pep_counter = dict()
            total_counter = 0
            for row in reader:
                status_text = row[2]
                if status_text not in pep_counter.keys():
                    pep_counter[status_text] = 1
                else:
                    pep_counter[status_text] += 1
            pep_counter.pop('status', '')
            # for status, count in pep_counter.items():
            #     total_counter += count
            # print(pep_counter)


            with open(STATUSES_FILENAME, mode='w', encoding='utf-8') as f:
                # Записываем строки в csv-файл. Колонки разделяются запятой, без пробелов.
                f.write('Статус,Количество\n')
                for status, count in pep_counter.items():
                    total_counter += count
                    f.write(f'{status},{count}\n')
                # print(pep_counter)
                f.write(f'Total,{total_counter}\n')
