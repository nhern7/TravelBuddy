from django.shortcuts import get_list_or_404,render
from .models import Destination  #import the Destination class from models

# Create your views here. connects to the app urls
# "dynamic" meaning data is coming from somewhere not static, can be easily updated
# "render" meaning give us the page with the data we want
# last argument^^ is the data we want to pass in during rendering
    
def index(request):
    dests = get_list_or_404(Destination)

    #couldve done {'price': 610} to refer to this price in our html...static to dynamic
    return render(request, 'travello/index.html', {'dests':dests})  #{} to load and define data. will refer to it as "dests"

def register(request):
    return render(request, 'acconuts/register.html')