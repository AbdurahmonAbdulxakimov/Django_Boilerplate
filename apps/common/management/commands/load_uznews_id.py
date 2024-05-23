import json
import time

from django.core.management.base import BaseCommand

from apps.news.models import Content


class Command(BaseCommand):
    help = 'Load uznews id'

    def handle(self, *args, **options):
        begin = time.time()
        cnt = 0
        with open("posts_dict.json", "r") as json_file:
            posts_data = json.load(json_file)
        print("STARTED ...")
        for content in Content.objects.all():
            if content.slug:
                _id = posts_data.get(content.slug, None)
                if _id:
                    content.uznewsuz_id = _id
                    content.save()
                    cnt += 1
            if cnt % 1000 == 0:
                print(f"Processed {cnt} records")
        self.stdout.write(self.style.SUCCESS(f"Time elapsed: {time.time() - begin:.2f} seconds."))
