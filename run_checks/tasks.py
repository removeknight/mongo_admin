import string

from agency_users.models import User, Agency
from django.utils.crypto import get_random_string
from celery import shared_task
from datetime import date


@shared_task
def create_random_user_accounts(total):
    uid = User.objects.last().uid + 1
    for i in range(total):
        uid += 1
        name = 'user_{}'.format(get_random_string(4, string.ascii_letters))
        email = '{}@example.com'.format(name)
        start_date = date(2019, 1, 30)
        User.objects.create(uid=uid, name=name, email=email, start_date=start_date)
    return '{} random users created successfully'.format(total)

