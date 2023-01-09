from django.core.management.base import BaseCommand

from collections import defaultdict
import csv

from ...models import ArtistModel, ArtModel


class Command(BaseCommand):
    help = 'Convert csv'

    def handle(self, *args, **kwargs):
        art_dict = defaultdict(list)
        with open('../Art.csv', encoding='utf-8', mode='r') as csv_file:
            rdr = csv.reader(csv_file, delimiter=',')
            for _, row in enumerate(rdr):
                if not _: continue

                id_, artist_name, year, desc, url_ = int(row[0]), row[1], row[2], row[3], None
                if not artist_name:
                    artist_name = "(Others)"
                
                for val in row:
                    if 'upload.wikimedia' in val:
                        url_ = val
                        break
                else:
                    continue
                
                # just in case
                artist_name = artist_name.strip().replace('/', ' - ')

                new_dict = {}
                new_dict['id'] = id_
                new_dict['year'] = year if year else '(no year)'
                new_dict['desc'] = desc
                new_dict['url']  = url_
                art_dict[artist_name].append(new_dict)


        # json to database
        ArtistModel.objects.all().bulk_create(
            [
                ArtistModel(name=artist_name)
                for artist_name in art_dict
            ]
        )
        
        for artist in ArtistModel.objects.all():
            ArtModel.objects.all().bulk_create(
                [
                    ArtModel(artist=artist, year=item['year'], desc=item['desc'], url=item['url'], orig_id=item['id'])
                    for item in art_dict[artist.name]
                ]
            )
