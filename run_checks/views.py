from django.shortcuts import render, redirect

from .forms import GenerateRandomUserForm
# from agency_users.tasks import create_random_user_accounts
from run_checks.tasks import create_random_user_accounts
from agency_users.models import User


def all_users(request):
    all_users = User.objects.all()
    return render(request, 'users_list.html', {'all_users': all_users})


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




