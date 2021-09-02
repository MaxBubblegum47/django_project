from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, request
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment, Category, Report
from .forms import CommentForm, PostForm, ReportForm

from django.core.mail import EmailMessage, send_mail

@login_required
def SearchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues_title = Post.objects.filter(title__icontains=searched)
        venues_author = Post.objects.filter(author__username__icontains=searched)
        venues_tag = Post.objects.filter(author__blog_post__category__icontains=searched)
        if venues_title.exists():
            return render(request, 'search_venues.html', {'searched':searched, 'venues':venues_title})
        elif venues_author.exists():
            return render(request, 'search_venues.html', {'searched':searched, 'venues': venues_author})
        elif venues_tag.exists():
            return render(request, 'search_venues.html', {'searched':searched, 'venues':venues_tag})
    else:
        return render(request, 'search_venues.html', {})

@login_required
def ReportView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.post = post
            report.save()
            msg = '''Hello, new deli customer service autore: '''
            send_mail("Hello", "prova", "lorenzostigliano@gmail.com", ["lorenzostigliano@yahoo.com", ], fail_silently=False)
            return redirect('post-detail', pk=post.pk)
    else:
        form = ReportForm()
    return render(request, 'report_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)  # user likes this post
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


#def home(request):
#    context = {
#        'posts': Post.objects.all().order_by("-date_posted")
#    }
#    return render(request, 'home.html', context)

class Homeview(ListView):
    model = Post
    template_name = 'user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-date_posted')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Homeview, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    context = {
        'posts': Post.objects.filter(category=cats.replace("-", " ")).order_by("-date_posted")
    }
    return render(request, 'categories.html', context)

    #category_post = Post.objects.filter(category=cats)
    #return render(request, 'categories.html', {'cats': cats, 'category_post': category_post})


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserPostListView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, *args, **kwargs):
        likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes.total_likes()
        context = super(PostDetailView, self).get_context_data()
        context["total_likes"] = total_likes
        return context

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = "__all__"
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostCreateView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = "category_create.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryCreateView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context
