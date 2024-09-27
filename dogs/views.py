from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from dogs.models import Dog


class DogListView(ListView):
    model = Dog


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'breed', 'date_born', 'photo')
    success_url = reverse_lazy('dogs:dogs_list')
