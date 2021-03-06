
from django.http import request
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.contrib.auth.models import User


def home(request):
    content = {
        'posts': Post.objects.all(),
        'title': 'Home Blog'
    }
    return render(request, 'blog/home.html', content)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<list>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<list>.html
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


def base(request):
    return render(request, 'blog/base.html')
