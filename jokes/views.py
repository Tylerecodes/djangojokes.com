from django.views.generic import (
    CreateView, DeleteView, UpdateView, DetailView, ListView
)
from .models import Joke
from django.urls import reverse_lazy

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke
