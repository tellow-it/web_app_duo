from django.shortcuts import render
from django.views.generic import TemplateView
import telegram  # this is from python-telegram-bot package

from django.conf import settings
from django.template.loader import render_to_string


class IndexView(TemplateView):
    template_name = "main/index.html"


class AboutView(TemplateView):
    template_name = "main/about.html"


class BlogView(TemplateView):
    template_name = "main/blog.html"


class ContactView(TemplateView):
    template_name = "main/contact.html"


class FeedBackView(TemplateView):
    template_name = "main/feedback.html"



