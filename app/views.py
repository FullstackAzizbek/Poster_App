from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import * 
def homepage(request):
    return render(request, 'base.html')
def homepage_2(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        user = request.user
        info = Post(title = title,user = user, text = text)
        info.save()
        redirect('/user')
    posts = Post.objects.filter(user = request.user).all()
    
    return render(request, 'base2.html', {'posts': posts})

def loginpage(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password-repeat']
        
        if User.objects.filter(username=username).exists():  
            form = "Bu username bazada mavjud!"
            return render(request, 'register.html', {'form': form})
        if password != password2:
            form = "Parollar mos kelmadi!"
            return render(request, 'register.html', {'form': form})
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('/login')
    
    return render(request, 'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Pass request object to login()
            return redirect('/user')
        else:
            form = "Username yoki parol xato!"
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def delete_post(request, user, id):
    Post.objects.filter(user= user, id = id).delete()
    return redirect('/user')
def update_post(request, user, id):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        Post.objects.filter(user=user, id=id).update(title=title, text=text)
        return redirect('/user')

    form = Post.objects.get(user=user, id=id)
    return render(request, 'update.html', {'form': form})
    