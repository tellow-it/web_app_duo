import requests
from django.views.generic import TemplateView, CreateView, ListView
from django.conf import settings

from main.forms import FeedBackForm
from main.models import FeedBack, Post
from main.telegram import telegram_bot_send_text


class IndexView(TemplateView):
    template_name = "main/index.html"


class AboutView(TemplateView):
    template_name = "main/about.html"


class ContactView(TemplateView):
    template_name = "main/contact.html"


class FeedBackView(CreateView):
    template_name = "main/feedback.html"
    model = FeedBack
    success_url = '/'
    form_class = FeedBackForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        print(f'Name: {data["name"]}, Mail: {data["email"]}, Text: {data["message"]}')
        telegram_bot_send_text(data["name"], data["email"], data["message"])
        return super().form_valid(form)


class PostList(ListView):
    template_name = "main/blog.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 5
