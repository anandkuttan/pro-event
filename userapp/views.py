from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register/')  # Check your URL name in urls.py
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register/')  # Check your URL name in urls.py
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully created")
                return redirect('/')  # Check your URL name in urls.py
        else:
            messages.info(request, "Passwords don't match")
            return redirect('register/')  # Check your URL name in urls.py
    else:
        return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login success")
            return redirect('/')  # Check your URL name in urls.py
        else:
            messages.info(request,"Invalid credentials")
            return redirect('register/')  # Check your URL name in urls.py

    return render(request, 'log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')  # Check your URL name in urls.py
