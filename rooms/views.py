from django.shortcuts import render
from . import models as room_models


def all_rooms(request):
    all_rooms = room_models.Room.objects.all()
    return render(request, "rooms/all_rooms.html", context={"AR": all_rooms})
