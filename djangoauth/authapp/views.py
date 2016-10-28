from django.shortcuts import render
from forms import CreateUserForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

def create_user_view(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'create_user.html', {'form': form})
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['password_repeat']

            if password == confirm_password:
                # check if user exists
                user = User.objects.filter(username=email).first()
                if not user:
                    new_user = User.objects.create_user(
                        username=email,
                        email=email,
                        password=password
                    )
                    new_user.save()
                    return JsonResponse({
                        'data': 1
                    })
                else:
                    return JsonResponse({
                        'data': -1
                    })
            else:
                error = {
                    'msg': 'Passwords are not the same'
                }
                return render(request, 'create_user.html', {
                    'form': form,
                    'error': error
                })




def login_view(request):
    pass

def home_view(request):
    pass
