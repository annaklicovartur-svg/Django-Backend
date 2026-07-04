from django.shortcuts import render, redirect
from .models import *
from .forms import *
# from django.http import HttpResponse

# HttpResponse = Line, not a lot of informations
# render = for HTML showing

def bitch(request):
    # Logic of getting information 
    tasks = Task.objects.order_by('-id')[:5 ]
    return render(request, 'app/index.html', {'title': 'main page of a website', 'tasks': tasks})

def boodstrap(request):
    return render(request, 'app/boods.html')

def workshowing (request):
    works = Work.objects.all()
    return render(request, 'app/worksh.html', {
        'name': 'Work statistic', 
        'works': works
        }
        )

def create(request):
    error = ''
# Here is the logic to add the task in the database 
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/render')
        else:
            error = 'Form is incorrect'


# here we associate the fields from the FORM with DJANGO
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'app/create.html', context)


# 1. make error = '' 
# 2. check if request method is POST 
# 3. add form with request.POST  
# 4. check if its valid if it is save 
# 5. return redirect / else error

# 6. conect form with Your castom form 
# 7. and the context dictionary with your form


def creatework(request):
    error = ''
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/work')
        else:
            error = 'form is incorrect'
    
    form = WorkForm()
    context = {
        "form": form
    }
    return render(request, 'app/creatework.html', context)