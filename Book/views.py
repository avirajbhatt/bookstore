from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ImageForm
from .models import Book
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect("login")

    context = {'form': form}
    return render(request, 'signup.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password incorrect.")

    return render(request, "login.html")


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def addbook(request):
    form = ImageForm
    context = {'form': form}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    return render(request, 'addbook.html', context)


@login_required(login_url='login')
def showbook(request):
    products = Book.get_all_books()
    data = {'products': products}
    return render(request, 'showbook.html', data)


@login_required(login_url='login')
def thankyou(request):
    return render(request, 'thankyou.html')
