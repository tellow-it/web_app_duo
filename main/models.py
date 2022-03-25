from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email