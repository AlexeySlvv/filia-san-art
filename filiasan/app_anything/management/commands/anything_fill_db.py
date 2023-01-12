import os

from django.core.management.base import BaseCommand
from ...models import SeasonModel, DirectoryModel, AnythingModel


class Command(BaseCommand):
    help = 'Fill anything database'

    def handle(self, *args, **kwargs):
        #  anything\
        #    <Season>\
        #      <date_time>\
        #        prompt.txt
        #        image1.png
        #        image2.png
        anything_dir = r"media/anything/"
        season_dirs = [ 
            s for s in os.listdir(anything_dir) 
            if os.path.isdir(os.path.join(anything_dir, s)) 
        ]

        for season_dir in season_dirs:
            season = SeasonModel.objects.filter(name=season_dir).first()
            if not season:
                season = SeasonModel(name=season_dir)
                season.save()

            dir = os.path.join(anything_dir, season_dir)
            prompt_dirs = [ 
                p for p in os.listdir(dir) 
                if os.path.isdir(os.path.join(dir, p)) 
            ]

            for prompt_dir in prompt_dirs:
                dir = os.path.join(anything_dir, season_dir, prompt_dir)

                with open(os.path.join(dir, "prompt.txt"), "r", encoding="utf-8") as f_prompt:
                    prompt = f_prompt.read().strip()
                    prompt = ", ".join(sorted(prompt.split(", ")))

                directory = DirectoryModel.objects.filter(name=prompt_dir, prompt=prompt).first()
                if not directory:
                    directory = DirectoryModel(name=prompt_dir, prompt=prompt, season=season)
                    directory.save()

                image_list = [ i for i in os.listdir(dir) if i.endswith(".png") ]
                for image_name in image_list:
                    anything = AnythingModel.objects.filter(name=image_name).first()
                    if not anything:
                        anything = AnythingModel(directory=directory, name=image_name)
                        anything.save()
