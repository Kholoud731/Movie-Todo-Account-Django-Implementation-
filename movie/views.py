from django.forms.widgets import CheckboxInput
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie
from .forms import AddForm

# Create your views here.

def home(request):
    all_movies = Movie.objects.all()
    return render(request, 'movie/home.html', context={'d': all_movies})


def movie_view(request, id):
    movie = Movie.objects.get(id = id)
    return render(request, 'movie/movie.html', context={'d':movie})  

def movie_Add(request):
    dataform = AddForm()
    if request.method == 'POST':
        print(request.POST)
        dataform = AddForm(request.POST, request.FILES)
        if dataform.is_valid():
            print(request.POST)

            dataform.save()
            return redirect('home/')

        else:
            print(dataform.errors.as_data())     
        
    return render(request, 'movie/form.html', context={'af': AddForm})  

def movie_edit(request, **kwargs):
    print(kwargs['pk'])
    movie = Movie.objects.get(id=kwargs['pk'])
    form = AddForm(instance=movie)
    movie_form = AddForm(request.POST, request.FILES, instance=movie)
    if movie_form.is_valid():
        movie_form.save()
        return redirect('movie:home') 
    return render(request, 'movie/edit.html', context={'af': form})


def movie_delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movie:home')

 
    