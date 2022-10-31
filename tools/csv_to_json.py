from collections import defaultdict
import csv
import json

if __name__ == '__main__':
    art_dict = defaultdict(list)
    with open('Art.csv', encoding='utf-8', mode='r') as csv_file:
        rdr = csv.reader(csv_file, delimiter=',')
        for _, row in enumerate(rdr):
            id_, artist, year, desc, url_ = row[0], row[1], row[2], row[3], None
            if not artist:
                artist = "(Others)"
            
            for val in row:
                if 'upload.wikimedia' in val:
                    url_ = val
                    break
            else:
                continue
            
            # just in case
            artist = artist.strip().replace('/', ' - ')

            new_dict = {}
            new_dict['id'] = id_
            new_dict['year'] = year if year else '(no year)'
            new_dict['desc'] = desc
            new_dict['url']  = url_
            art_dict[artist].append(new_dict)
            
    with open('Art.json', encoding='utf-8', mode='w+') as json_file:
        json.dump(art_dict, json_file, ensure_ascii=False, indent=4)
        