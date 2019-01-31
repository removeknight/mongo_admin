from django.shortcuts import render, redirect

from .forms import GenerateRandomUserForm, GenerateRandomAgencyForm
from agency_users.tasks import create_random_user_accounts, create_random_agency_accounts
from agency_users.models import User, Agency
import redis
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def all_users(request):
    conn = redis.Redis()
    if not conn.get('all_users'):
        all_users = User.objects.all()
        users_json_data = serializers.serialize('json', all_users, cls=DjangoJSONEncoder)
        conn.setex('all_users', json.dumps(users_json_data), 10)
    else:
        users_json_data = json.loads(conn.get('all_users'))
        deser_data = serializers.deserialize('json', users_json_data, cls=DjangoJSONEncoder)
        all_users = [ele.object for ele in deser_data]
    return render(request, 'users_list.html', {'all_users': all_users})

def all_agencies(request):
    all_agencies = Agency.objects.all()
    return render(request, 'agencies_list.html', {'all_agencies': all_agencies})

def generate_agencies(request):
    if request.method == 'POST':
        form = GenerateRandomAgencyForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total')
            create_random_agency_accounts.delay(total)
            return redirect('all_agencies')
    else:
        form = GenerateRandomAgencyForm()
        return render(request, 'generate_random_agencies.html', {'form': form})
    return render(request, 'generate_random_agencies.html', {'form': form})

def generate_users(request):
    if request.method == 'POST':
        form = GenerateRandomUserForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total')
            create_random_user_accounts.delay(total)
            return redirect('all_users')
    else:
        form = GenerateRandomUserForm()
        return render(request, 'generate_random_users.html', {'form': form})
    return render(request, 'generate_random_users.html', {'form': form})