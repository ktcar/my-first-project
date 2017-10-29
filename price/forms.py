from django import forms
from price.models import Items


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['isbnid', 'isbn', 'title', 'link', 'image', 'author', 'price', 'discount'
                  'publisher', 'pubdate', 'description', 'searchDate']