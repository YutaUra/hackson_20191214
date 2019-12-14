from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    min_time = models.PositiveIntegerField()
    max_time = models.PositiveIntegerField()
    min_cost = models.PositiveIntegerField()
    max_cost = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Filter(models.Model):
    class Meta:
        abstract = True

    class MoodChoice(models.TextChoices):
        SLOW = 'slow'
        HIGH = 'high'

    object_nature = models.BooleanField(
        '自然や景勝地',
    )
    object_bath = models.BooleanField(
        '温泉',
    )
    object_gourmet = models.BooleanField(
        'グルメ',
    )
    object_historic = models.BooleanField(
        '歴史・文化的遺産',
    )
    object_ = models.BooleanField(
        '自然や景勝地',
    )object_nature = models.BooleanField(
        '自然や景勝地',
    )object_nature = models.BooleanField(
        '自然や景勝地',
    )object_nature = models.BooleanField(
        '自然や景勝地',
    )object_nature = models.BooleanField(
        '自然や景勝地',
    )object_nature = models.BooleanField(
        '自然や景勝地',
    )
    mood = models.CharField(
        max_length=4,
        choices=MoodChoice.choices,
    )
    option = models.TextField()


class PlaceMeta(Filter):
    place = models.OneToOneField(to=Place, on_delete=models.CASCADE)
