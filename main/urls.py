from django.urls import path

from main.views import IndexView, AboutView, PostList, ContactView, FeedBackView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', PostList.as_view(), name="blog"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('feedback/', FeedBackView.as_view(), name="feedback"),

]
