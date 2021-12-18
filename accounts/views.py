from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already registered!!")
                return redirect('register')
            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                            password=password)
            user.save()
            print('user added!!')

        else:
            messages.info(request, "passwords not match!!")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print('found!!')
            print(user.is_authenticated)
            return redirect('/')
        else:
            print('not found')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
