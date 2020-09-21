from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    book_type = forms.ChoiceField(
        required=False,
        choices=[('', '----'), ] + Book.BookTypes.choices,
        widget=forms.Select(attrs={'class': "custom-select"}),
    )

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )
