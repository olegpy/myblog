from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from .models import Post, Comment


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['page_title'] = "Post list"
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Post detail"
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blogs/post_edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Post create"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.published_date = timezone.now()
        self.object.save()
        messages.success(
            self.request, 'Post %s has been add successfully.' % (self.object.title))
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', args=(self.object.pk,))


class CommentCreateView(CreateView):
    model = Comment
    fields = ['author', 'text']
    template_name = 'blogs/post_comment.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Add comments'
        return context

    def form_valid(self, form):
        self.object = objects
        objects = form.save(commit=False)
        objects.post = post
        objects.save()
        messages.success(
            self.request, 'Comment %s has been successfully.' % (objects.author))
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', args=(self.object.pk, ))


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blogs/post_edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = "Post update"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.published_date = timezone.now()
        self.object.save()
        messages.success(
            self.request, 'Post %s has been successfully edit.' % (self.object.title))
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', args=(self.object.pk,))


class PostDeleteView(DeleteView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blogs/post_remove.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = "Post deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(PostDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Post %s has been deleted.' % (
            self.object.title))
        return message


# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blogs/post_list.html', {'posts': posts})


# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     return render(request, 'blogs/post_detail.html', {'post': post})


# def add_post(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             messages.success(request, 'Post %s has been add successfully.' % (
#                 post.title))
#             return redirect('post_detail', post.id)
#     else:
#         form = PostModelForm()
#     return render(request, 'blogs/post_edit.html', {'form': form})

# def edit_post(request, pk):
#     post = Post.objects.get(id=pk)
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form .is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             messages.success(request, 'Post %s has been successfully edit.' % (
#                 post.title))
#             return redirect('post_detail', post.id)

#     else:
#         form = PostModelForm(instance=post)
#     return render(request, 'blogs/post_edit.html', {'form': form})
