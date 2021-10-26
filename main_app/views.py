from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    # get the list of todos
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    todos = response.json()
    return render(request, "main_app/home.html", {"todos": todos})
