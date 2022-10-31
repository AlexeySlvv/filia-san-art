import csv
import json
from pprint import pprint
from typing import OrderedDict

if __name__ == '__main__':
    art_dict = OrderedDict()
    with open('Art.csv', encoding='utf-8', mode='r') as csv_file:
        rdr = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(rdr):
            id_, artist, year, desc, url_ = row[0], row[1], row[2], row[3], None
            for val in row:
                if 'upload.wikimedia' in val:
                    url_ = val
                    break
            else:
                continue
            
            if artist not in art_dict:
                art_dict[artist] = []

            new_dict = {}
            new_dict['id'] = id_
            new_dict['year'] = year
            new_dict['desc'] = desc
            new_dict['url']  = url_
            art_dict[artist].append(new_dict)
            
    with open('Art.json', encoding='utf-8', mode='w+') as json_file:
        json.dump(art_dict, json_file, ensure_ascii=False, indent=4)
        