from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':'Faisal', 'age':25},
        {'name':'Wahab', 'age':24},
        {'name':'Ahtsham', 'age':23},
        {'name':'Fahad', 'age':28},
        {'name':'Shahzaib', 'age':27},
        {'name':'Noman', 'age':17},
    ]

    text = '''
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Doloribus, amet? Quaerat delectus vel ut veniam voluptatum molestias inventore illum quibusdam incidunt, aliquid ab id reiciendis dicta aliquam voluptates, cupiditate ex!
'''

    for people in peoples:
        print(people)
    return render(request, "index.html" , context= {'peoples' : peoples , 'text':text, 'page':'Django Home'})

def contact(request):
    context = {'page': 'Contact'}
    return render(request,"contact.html" , context)

def about(request):
    context = {'page': 'About'}
    return render(request,"about.html" , context)


def success_page(request):
    print('*' * 10)
    return HttpResponse("<h1>Hey this is a success page</h1>")