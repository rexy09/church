from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Register user View
def register_user(request, *args, **kwargs):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save(commit=False)
            passwd1 = form.cleaned_data.get('password1')
            passwd2 = form.cleaned_data.get('password2')

            if passwd1 == passwd2:

                user.set_password(passwd1)
                user.save()

                return redirect('accounts:list-user')

            else:
                messages.error(
                    request, "The two password fields didn’t match.")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register-user.html', context)


# User login view
def login_view(request, *args, **kargs):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            # Login Form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


# logout view
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('index')


# List users
def list_user(request, *args, **kwargs):
    user_list = User.objects.all().order_by('-id')
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        'users': users,
    }
    return render(request, 'list-user.html', context)


# View users
def view_user(request, *args, **kwargs):
    obj = User.objects.filter(id=kwargs.get('id')).first()

    context = {
        'obj': obj,
    }
    return render(request, 'view-user.html', context)


# Edit user
def edit_user(request, *args, **kwargs):
    user = User.objects.filter(id=kwargs.get('id')).first()

    if request.method == 'POST':
        form = UpdateUserForm(request.POST or None, instance=user)

        if form.is_valid():
            form.save()

            return redirect('accounts:list-user')

    else:
        form = UpdateUserForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'edit-user.html', context)


# Change password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST or None)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {'form': form})


# Delete users
def delete_user(request, *args, **kwargs):
    obj = User.objects.filter(id=kwargs.get('id')).first()

    if request.method == 'POST':
        obj.delete()

        return redirect('accounts:list-user')

    context = {
        'obj': obj,
    }
    return render(request, 'delete-user.html', context)

# My profile
@login_required
def profile_view(request, *args, **kwargs):
    obj = User.objects.filter(id=request.user.id).first()

    context = {
        'obj': obj,
    }   
    return render(request, 'profile-view.html', context)
