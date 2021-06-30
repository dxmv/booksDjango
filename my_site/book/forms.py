from django import forms
from .models import Genre,Book
class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields=["name"]
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "description",
            "published"
        ]