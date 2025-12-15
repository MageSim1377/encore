from django.db import models


class Rehearsals(models.Model):
    band_id = models.IntegerField("band id")
    rehearsal_date = models.DateTimeField("Date & time")
    duration = models.IntegerField("Duration")
    location = models.CharField("Location", max_length=255)

    def __str__(self):
        return self.rehearsal_date.__str__()
    

class Bands(models.Model):
    band_name = models.CharField("Band name", max_length=100)
    genre = models.CharField("Duration", max_length=50)
    founded_date = models.DateTimeField("Founded")

    def __str__(self):
        return self.band_name
    

class Band_membership(models.Model):
    band_id = models.IntegerField("Band id")
    musician_id = models.IntegerField("Musician id")
    join_date = models.DateTimeField("Joined")

    def __str__(self):
        return self.band_id
    

class Musicians(models.Model):
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)
    phone = models.CharField("Phone", max_length=20)
    telegram = models.CharField("Telegram", max_length=100)
    instrument = models.CharField("Instrument", max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Performances(models.Model):
    band_id = models.IntegerField("Band id")
    concert_id = models.IntegerField("Concert id")
    performance_order = models.IntegerField("Performance order")

    def __str__(self):
        return self.band_id


class Concerts(models.Model):
    concert_title = models.CharField("Title", max_length=200)
    venue_address = models.CharField("Address", max_length=255)
    concert_date = models.DateTimeField("Date")

    def __str__(self):
        return self.concert_title