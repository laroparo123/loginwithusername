
from django.shortcuts import render
from django.http import HttpResponse
from . models import books
# Create your views here.
# Create your views here.


def home(request):
    book = books.objects.all()
    print(book)

    return render(request, 'base.html', {'books': book})
