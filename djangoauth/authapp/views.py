from django.shortcuts import render
from forms import CreateUserForm
from django.http import HttpResponse, JsonResponse

def create_user_view(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'create_user.html', {'form': form})
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['password_repeat']

            if password == confirm_password:
                return JsonResponse({
                    'data': 1
                })
            else:
                return JsonResponse({
                    'data': 0
                })




def login_view(request):
    pass

def home_view(request):
    pass
