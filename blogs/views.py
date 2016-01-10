from django.utils import timezone
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blogs/post_edit.html'
    context_object_name = 'form'

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


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blogs/post_edit.html'
    context_object_name = 'form'

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
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Post deletion"
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
