from django.shortcuts import render, redirect
from django.contrib.auth import login as authlogin, logout as authlogout, authenticate
from django.contrib.auth.hashers import make_password
from .models import Users
from django.core.mail import send_mail
# Create your views here.
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        avatar = request.POST['avatar']
        user = Users(first_name=firstname, last_name=lastname, username=username, password=make_password(password), email=email, avatar=avatar)
        user.save()
        subject = 'Bienvenue sur notre site'
        message = 'Merci de vous être inscrit à notre site.'
        from_email = 'sebreyes222@gmail.com'           
        to_email = user.email
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        authlogin(request, user)
        return redirect('home')
    return render(request, 'projetfinal/connexion/signup.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authlogin(request, user)
            return redirect('home')
        else:
            error = "pas bon"
            return render(request, 'projetfinal/connexion/login.html', {'error': error})
    return render(request, 'projetfinal/connexion/login.html')

def logout(request):
    authlogout(request)
    return redirect('home')