from django.views.generic import (
    CreateView, DeleteView, UpdateView, DetailView, ListView
)
from .models import Joke
from django.urls import reverse_lazy
from .forms import JokeForm


class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm


class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')


class JokeListView(ListView):
    model = Joke


class JokeDetailView(DetailView):
    model = Joke
