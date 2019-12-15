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
        '自然や景勝地',        default=False,

    )
    object_bath = models.BooleanField(
        '温泉',        default=False,

    )
    object_gourmet = models.BooleanField(
        'グルメ',        default=False,

    )
    object_historic = models.BooleanField(
        '歴史・文化的遺産',        default=False,

    )
    object_shopping = models.BooleanField(
        'ショッピング',        default=False,

    )
    object_zoo_aquarium = models.BooleanField(
        '動物園・水族館',        default=False,

    )
    object_art = models.BooleanField(
        '美術館・博物館',        default=False,

    )
    object_sport = models.BooleanField(
        'スポーツ・アクティビティ',
        default=False,

    )
    object_other = models.BooleanField(
        'その他',
        default=False,

    )
    object_any = models.BooleanField(
        '何でもよい',
        default=False,
    )
    mood = models.CharField(
        max_length=4,
        choices=MoodChoice.choices,
    )
    option = models.TextField()


class PlaceMeta(Filter):
    place = models.OneToOneField(to=Place, on_delete=models.CASCADE)
