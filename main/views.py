import requests
from django.views.generic import TemplateView, CreateView
from django.conf import settings

from main.forms import FeedBackForm
from main.models import FeedBack


class IndexView(TemplateView):
    template_name = "main/index.html"


class AboutView(TemplateView):
    template_name = "main/about.html"


class BlogView(TemplateView):
    template_name = "main/blog.html"


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


def telegram_bot_send_text(username, mail, text):
    bot_token = settings.TELEGRAM.get('bot_token')
    bot_chatID = settings.TELEGRAM.get('channel_id')
    message = f'Username: {username} \nMail: {mail} \nText: {text}'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + message

    return requests.get(send_text).json()


