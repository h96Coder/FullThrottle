from django.core.management.base import BaseCommand, CommandError
from FullThrottleApp.models import User
from FullThrottleApp.models import ActivityPeriod
from faker import  Faker
from random import randint
import random


class Command(BaseCommand):
    help = 'populate data'
    def user_id(self):
        fake = Faker()
        id="".join([random.choice(list(f"{str(fake.name().strip()).upper()[:6].strip()}{randint(1000, 9999)}"))for i in range(10)])
        return id

    def handle(self, *args, **options):
        fake=Faker()
        print("User Creating :",end=" ")
        for x in range(100):
            print(x,end=" ")
            id=self.user_id()
            user=User(id=id,real_name=fake.name(),tz=fake.country()+"/"+fake.city())
            user.save()
            ran=random.randrange(1,5);
            for i in range(ran):
                month = fake.month()[:3]
                day =fake.day_of_month()
                year=fake.year()
                time= fake.time(pattern='%H:%M')
                pm_am=fake.am_pm()
                activity=ActivityPeriod(user_id=user,start_time=month+" "+str(int(day))+" "+year+ " "+time+pm_am,end_time=fake.month()[:3]+" "\
                                        +fake.day_of_month()+" "+str(int(year)+1)+" "+fake.time(pattern='%H:%M')+fake.am_pm())
                activity.save()

        #print(ActivityPeriod.objects.values())
