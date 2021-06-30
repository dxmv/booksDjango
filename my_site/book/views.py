from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Genre,Book
from .forms import GenreForm,BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
def check_owner(user,owner):
    if user!=owner:
        raise Http404
def home(request):
    return render(request,"book/home.html")
@login_required
def genres(request):
    genres=Genre.objects.all().filter(owner=request.user).order_by('date_added')
    context={"genres":genres}
    return render(request,"book/genres.html",context)
@login_required
def books(request,genre_id):
    genre=Genre.objects.get(id=genre_id)
    books=genre.book_set.all()
    context={"genre":genre,"books":books}
    return render(request,"book/genre.html",context)
@login_required
def new_genre(request):
    genres=Genre.objects.all().filter(owner=request.user)
    if request.method=="POST":
        form=GenreForm(request.POST)
        if form.is_valid():
            g=form.save(commit=False)
            g.owner=request.user
            if Genre.objects.all().filter(name=g.name).exists() and g in genres:
                messages.info(request,"That genre already exists!")
            else:
                g.save()
                messages.success(request,"New genre added!")
                return HttpResponseRedirect(reverse("book:genres"))
        else:
            messages.info(request,"There was an error!")
    else:
        form=GenreForm()
    context={"form":form}
    return render(request,"book/new_genre.html",context)
@login_required
def new_book(request,genre_id):
    genre=Genre.objects.get(id=genre_id)
    check_owner(request.user,genre.owner)
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.genre=genre
            if Book.objects.all().filter(genre=new_entry.genre).filter(title=new_entry.title).exists():
                messages.info(request, "That book already exists!")
            else:
                new_entry.save()
                messages.success(request, "New book added!")
                return HttpResponseRedirect(reverse("book:books",args=[genre.id]))
        else:
            messages.info(request,"There was an error!")
    else:
        form=BookForm()
    return render(request,"book/new_book.html",{"form":form,"genre":genre})
@login_required
def edit_book(request,book_id):
    book=Book.objects.get(id=book_id)
    genre=book.genre
    check_owner(request.user,genre.owner)
    if request.method=="POST":
        form=BookForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book edited!")
            return HttpResponseRedirect(reverse("book:books",args=[genre.id]))
        else:
            messages.info(request, "There was an error!")
    else:
        form=BookForm(instance=book)
    context={"form":form,"genre":genre,"book":book}
    return render(request,"book/edit_book.html",context)

def edit_genre(request,genre_id):
    genre=Genre.objects.all().get(id=genre_id)
    check_owner(request.user, genre.owner)
    if request.method=="POST":
        form = GenreForm(instance=genre,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Genre edited!")
            return redirect("/genres/")
        else:
            messages.info(request, "There was an error!")
    else:
        form=GenreForm(instance=genre)
    return render(request,"book/edit_genre.html",{"form":form,"genre":genre})

def delete_genre(request,genre_id):
    genre=Genre.objects.all().get(id=genre_id)
    check_owner(request.user, genre.owner)
    if request.method=="POST":
        genre.delete()
        messages.success(request,"Genre was deleted")
        return redirect("/genres/")
    return render(request,"book/delete_genre.html",{"genre":genre})
def delete_book(request,book_id):
    book=Book.objects.all().get(id=book_id)
    genre=book.genre
    if request.method=="POST":
        book.delete()
        messages.success(request,"Book was deleted")
        return redirect(f"/genres/{genre.id}")
    return render(request,"book/delete_book.html",{"book":book,"genre":genre})






