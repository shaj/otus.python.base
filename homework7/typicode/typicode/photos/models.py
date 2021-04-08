from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from ..posts import MY_TEST_VAR
# from ..posts import User

class User(models.Model):
    pass

# Create your models here.
class Album(models.Model):

    user_id = models.ForeignKey(User, on_delete=PROTECT)
    title = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    def update_jsonplaceholder(self, data: dict):
        try:
            self.id = int(data["id"])
        except Exception:
            pass
        try:
            self.user_id = int(data["userId"])
        except Exception:
            pass
        self.title = data["title"]


class Photo(models.Model):

    album_id = models.ForeignKey(User, on_delete=PROTECT)
    title = models.CharField(128)
    url = models.CharField(256)
    thumbnailUrl = models.CharField(256)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    def update_jsonplaceholder(self, data: dict):
        try:
            self.id = int(data["id"])
        except Exception:
            pass
        try:
            self.album_id = int(data["albumId"])
        except Exception:
            pass
        self.title = data["title"]
        self.url = data["url"]
        self.thumbnailUrl = data["thumbnailUrl"]
