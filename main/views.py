from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from main.forms import FeedBackForm
from main.models import FeedBack, Post
from main.telegram import telegram_bot_send_text

try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            post.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a company
            post.likes.add(user)
            message = 'You liked this'

        ctx = {'total_likes': post.total_likes, 'message': message}
        # use mimetype instead of content_type if django < 5
        return HttpResponse(json.dumps(ctx), content_type='application/json')


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
    paginate_by = 2
    queryset = Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(DetailView):
    model = Post
    template_name = "main/post_detail.html"
