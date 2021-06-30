from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm,EditUserForm
def register(request):
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfuly")
            return redirect("/login/")
        else:
            messages.info(request,"There was an error!")
    else:
        form=RegistrationForm()
    return render(request,"users/registration.html",{"form":form})
def account(request):
    return render(request,"users/account.html")
def edit_user(request):
    if request.method=="POST":
        form=EditUserForm(instance=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Edit was successful")
            return redirect("/account/")
    else:
        form=EditUserForm(instance=request.user)
    return render(request,"users/edit_user.html",{"form":form})
# Create your views here.
