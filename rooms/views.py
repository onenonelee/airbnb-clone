from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    print(page)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    end_page = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/all_rooms.html",
        context={"AR": all_rooms, "current_page": page, "end_page": end_page},
    )
