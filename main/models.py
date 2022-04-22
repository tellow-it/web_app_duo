from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email


class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    information = models.TextField()
    image = models.ImageField(upload_to="media/post_image")

    def __str__(self):
        return f'{self.id}__{self.name}__{self.description}__{self.information}__{self.image}'
