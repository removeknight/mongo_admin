import string

from agency_users.models import User, Agency
from django.utils.crypto import get_random_string
from celery import shared_task
from datetime import datetime
import random


@shared_task
def create_random_user_accounts(total):
    agency_objs = Agency.objects.all()
    all_licenses = ['google', 'office', 'okata', 'adobe', 'former', 'employee']
    uid = 0 if not User.objects.last() else User.objects.last().uid + 1
    for i in range(total):
        uid += 1
        name = 'user_{}'.format(get_random_string(4, string.ascii_letters))
        email = '{}@example.com'.format(name)
        start_date = datetime.now().date()
        licenses = random.sample(all_licenses, 3)
        agency = random.choice(agency_objs)
        User.objects.create(uid=uid, name=name, email=email, agency = agency,
                            start_date=start_date, licenses = licenses)
    return '{} random users created successfully'.format(total)

@shared_task
def create_random_agency_accounts(total):
    for i in range(total):
        location_code = str(i)
        name = 'Agency_{}'.format(get_random_string(4, string.ascii_letters))
        Agency.objects.create(location_code=location_code, name=name)
    return '{} random agencies created successfully'.format(total)



