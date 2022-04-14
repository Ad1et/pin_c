from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def index(request):
    #context = {'pins_on_board', Pin.objects.all()}
    return render(request, 'main.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(username=username, first_name=uname, last_name=surname,
                                           email=email, password=pass1)
                user.save()
                if user is not None:
                    auth.login(request, user)
                    return render(request, 'cabinet.html')

        else:
            messages.error(request, "Both password are not matching")
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'cabinet.html')
        else:
            messages.error(request, "Invalid Username or Password")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')


def cabinet(request):
    return render(request, 'cabinet.html')


'''def get_pin_by_id(request, id):
    try:
        pin = Pin.objects.get(id)
    except:
        return HttpResponse(f"No such pin with id #{id}")
    return HttpResponse(f"Pin with id {id}: <br> {pin.desctription}")
'''