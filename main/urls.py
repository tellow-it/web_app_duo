from django.urls import path

from main.views import IndexView, AboutView, BlogView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', BlogView.as_view(), name="blog")

]
