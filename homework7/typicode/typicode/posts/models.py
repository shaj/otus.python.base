from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class User(models.Model):

    fullname = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    website = models.CharField(max_length=128)

    street = models.CharField(max_length=32)
    suite = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    geo_lat = models.CharField(max_length=32)
    geo_lng = models.CharField(max_length=32)

    company_name = models.CharField(max_length=32)
    company_catchPhrase = models.CharField(max_length=128)
    company_bs = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    # def __repr__(self):
    #     return str(self)

    def update_jsonplaceholder(self, data: dict):
        try:
            self.id = int(data["id"])
        except Exception:
            pass
        self.fullname = data["name"]
        self.username = data["username"]
        self.email = data["email"]
        self.street = data["address"]["street"]
        self.suite = data["address"]["suite"]
        self.city = data["address"]["city"]
        self.zipcode = data["address"]["zipcode"]
        self.geo_lat = data["address"]["geo"]["lat"]
        self.geo_lng = data["address"]["geo"]["lng"]
        self.phone = data["phone"]
        self.website = data["website"]
        self.company_name = data["company"]["name"]
        self.company_catchPhrase = data["company"]["catchPhrase"]
        self.company_bs = data["company"]["bs"]


class Todo(models.Model):

    user_id = models.ForeignKey(User, on_delete=PROTECT)
    title = models.TextField()
    completed = models.BooleanField(null=False, default=False)

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
        self.completed = data["completed"]


class Post(models.Model):

    user_id = models.ForeignKey(User, on_delete=PROTECT)
    title = models.CharField(max_length=256, null=False)
    body = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title})"

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
        self.body = data["body"]


class Comment(models.Model):

    post_id = models.ForeignKey(Post, on_delete=PROTECT)
    name = models.CharField(max_length=128, null=False)
    email = models.CharField(max_length=128, null=False)
    body = models.TextField()

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
            self.post_id = int(data["postId"])
        except Exception:
            pass
        self.name = data["name"]
        self.email = data["email"]
        self.body = data["body"]


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
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=256)
    thumbnailUrl = models.CharField(max_length=256)

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
