import json
import time

from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = 'Load users avatar'

    def handle(self, *args, **options):
        begin = time.time()
        cnt = 0
        cnt2 = 0
        with open("users.json", "r") as json_file:
            user_data = json.load(json_file)
        print("STARTED ...")
        for user in User.objects.all():
            user_info = user_data.get(user.password)
            if not user_info:
                continue
            avatar = user_info.get("avatar")
            _id = user_info.get("id")
            if avatar:
                user.avatar = avatar
                user.save()
                cnt += 1
            if _id:
                user.uznewsuz_id = _id
                user.save()
                cnt2 += 1
            if cnt % 1000 == 0:
                print(f"Processed {cnt} records")
            if cnt2 % 1000 == 0:
                print(f"Processed {cnt2} user ids")

        self.stdout.write(self.style.SUCCESS(f"Time elapsed: {time.time() - begin:.2f} seconds."))
