from django.urls import path

from main import views
from main.views import IndexView, AboutView, PostList, ContactView, FeedBackView, PostDetail

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', PostList.as_view(), name="blog"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('feedback/', FeedBackView.as_view(), name="feedback"),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/', views.like, name='like'),

]
