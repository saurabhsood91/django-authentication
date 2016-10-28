from django.shortcuts import render
from forms import CreateUserForm
from django.http import HttpResponse

def create_user_view(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'create_user.html', {'form': form})


def login_view(request):
    pass

def home_view(request):
    pass
