from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)
    subname = models.CharField(max_length=140, blank=True)

    class Meta:
        abstract = True

    # def __str__(self) shows how this model would look on the panel
    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    # We can config many things with the Meta class
    # i.e. we can config how it would show on the panel using verbose_name
    class Meta:
        verbose_name = "Room Type"
        ordering = ["-created"]


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    # i.e. and using verbose_name_plural would modify how it look when it's plural
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    # ForeignKey is a connection to something. it's OneToOne Relationship
    # on_delete=model.CASCADE => when "user_models.User" is deleted, the room also gets deleted
    # on_delete=model.PROTECTED => "user_models.User" is unable to get deleted
    # on_delete=model.SET_NULL => when "user_models.User" is deleted, the room becomes orphan
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    # ManyToManyField makes the variable to have many Relationships(multiple options)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name
