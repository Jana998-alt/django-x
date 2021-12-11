from django.shortcuts import render

# Create your views here
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = "/-list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "/-detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "/-create.html"
    model = Snack
    fields = []


class SnackUpdateView(UpdateView):
    template_name = "/-update.html"
    model = Snack
    fields = []


class SnackDeleteView(DeleteView):
    template_name = "/-delete.html"
    model = Snack
    success_url = reverse_lazy("_list")