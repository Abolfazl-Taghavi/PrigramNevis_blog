from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


def home_view(request):
    return render(request, 'home.html')


class PostListView(generic.ListView):
    template_name = 'blogs/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_updated')


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blogs/post_detail.html'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blogs/post_create_or_update.html'


class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'blogs/post_create_or_update.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')
    template_name = 'blogs/post_delete.html'
