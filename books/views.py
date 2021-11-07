from django.shortcuts import render
from django.http import HttpResponse

import json
from books.models import Book

bookData = open('./books.json').read()

data = json.loads(bookData)

# Create your views here.
def index(request):
    bdData = Book.objects.all()
    context = {'bdata': data}
    return render(request,'books/index.htm',context)

def shows(request,id):

    singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book

    context = {'book': singleBook}
    return render(request,'books/shows.htm',context)

