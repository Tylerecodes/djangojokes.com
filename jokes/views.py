from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke
