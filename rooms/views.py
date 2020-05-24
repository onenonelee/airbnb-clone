from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class RoomView(ListView):

    """ RoomView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
