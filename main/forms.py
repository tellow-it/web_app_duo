from django.forms import ModelForm
from .models import FeedBack


class FeedBackForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = FeedBack
        # Поля, которые будем использовать для заполнения
        fields = ['name', 'email', 'message']
