from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Mixin is for updating posts
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {         # dictinary
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    # blog/post_list.html (see in a browser)
    # <app>/<model>_<viewtype>.html <app> - name 'blog' , <model> - name 'post'
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2 # how many posts in a page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    # if user excit we get empty otherwise error 404
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs. get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView): # inherit from createview
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # take instance and set author
        return super().form_valid(form) # validate form
            # super means do in a parent class

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # inherit from createview
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # take instance and set author
        return super().form_valid(form) # validate form
            # super means do in a parent class

            # is the user an author? 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailView(DetailView):
    model = Post
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # if success go to home

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

