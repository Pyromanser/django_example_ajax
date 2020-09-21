from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    class BookTypes(models.IntegerChoices):
        HARDCOVER = 1, _('Hardcover')
        PAPERBACK = 2, _('Paperback')
        EBOOK = 3, _("E-book")

    title = models.CharField(max_length=50)
    publication_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BookTypes.choices, blank=True, null=True)
