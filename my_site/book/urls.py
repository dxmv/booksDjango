from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("genres/",views.genres,name="genres"),
    path("genres/<genre_id>/",views.books,name="books"),
    path("new_genre/",views.new_genre,name="new_genre"),
    path("new_book/<int:genre_id>/",views.new_book,name="new_book"),
    path("edit_book/<int:book_id>/",views.edit_book,name="edit_book"),
    path("edit_genre/<int:genre_id>/",views.edit_genre,name="edit_genre"),
    path("delete_genre/<int:genre_id>/",views.delete_genre,name="delete_genre"),
    path("delete_book/<int:book_id>/",views.delete_book,name="delete_book")
]