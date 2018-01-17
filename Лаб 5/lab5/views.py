from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
data = {
    'books': [
        {'id': 1, 'name': 'Мастер и Маргарита', 'author':'Михаил Булгаков'},
        {'id': 2, 'name': 'Гобсек', 'author': 'Оноре Де Бальзак'},
        {'id': 3, 'name': 'Принц Амбера', 'author': 'Роберт Желязны'}
    ]
}
def function_view(request):
    return HttpResponse('response from function view')

class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')

class BooksView(View):
    def get(self, request):
        return render(request, 'listPage.html', data)

class BookView(View):
    def get(self, request, id):
        selectedBook = None
        for book in data['books']:
            if int(id) == book['id']:
                selectedBook = book
        return render(request, 'bookPage.html', selectedBook)
