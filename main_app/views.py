from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    # get the list of todos
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    todos = response.json()
    return render(request, "main_app/home.html", {"todos": todos})

# get to do by id
def todo_id(request):
    id = {}
    if 'id' in request.GET:
        id = request.GET['id']
        url = 'https://jsonplaceholder.typicode.com/todos'%id
        response = request.get(url)

        todo = response.json()
    return render(request, 'main_app/single_todo.html', {"todo":todo})

    