from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm


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

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     queryset = super(PostListView, self).get_queryset(
    #     ).order_by('created_date')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['page_title'] = "Post list"
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Post detail"
        context['comments'] = Comment.objects.filter(post=self.get_object().id)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blogs/post_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('post_list')

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

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('post_list', args=(self.object.pk,))


# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentModelForm
#     template_name = 'blogs/post_comment.html'
#     context_object_name = 'form'

#     def get_context_data(self, **kwargs):
#         context = super(CommentCreateView, self).get_context_data(**kwargs)
#         context['page_title'] = 'Add comments'
#         return context

#     def form_valid(self, form):
#         # link = get_object_or_404(Comment, pk=self.post.pk)
#         # print link

#         comment = form.save(commit=False)

#         name = form.cleaned_data

#         print self.request.post.id
#         # print self.request.post
#         # comment.post = self.post
#         comment.save()

#         # comment = form.save(commit=False)
#         # comment.author = self.request.post
#         # # self.object.published_date = timezone.now()
#         # comment.save()

#         data = form.cleaned_data
#         messages.success(
#             self.request, 'Comment %s has been successfully.' % (data[
#                                                                  'author']))
#         return super(CommentCreateView, self).form_valid(form)

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('post_detail', args=(self.object.pk, ))


#

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostModelForm
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
    form_class = PostModelForm
    template_name = 'blogs/remove.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = "Post deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(PostDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Comment has been deleted.')
        return message


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostModelForm
#     template_name = 'blogs/post_edit.html'
#     context_object_name = 'form'

#     def get_context_data(self, **kwargs):
#         context = super(PostCreateView, self).get_context_data(**kwargs)
#         context['page_title'] = "Post create"
#         return context

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.author = self.request.user
#         self.object.published_date = timezone.now()
#         self.object.save()
#         messages.success(
#             self.request, 'Post %s has been add successfully.' % (self.object.title))
#         return super(PostCreateView, self).form_valid(form)

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('post_list', args=(self.object.pk,))


def add_comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()
    return render(request, 'blogs/post_comment.html', {'form': form})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'blogs/post_comment.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CommentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = "Comment update"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        messages.success(
            self.request, 'Comment %s has been successfully edit.' % (self.object.post))
        return super(CommentUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', args=(self.object.pk,))


class CommentDeleteView(DeleteView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'blogs/remove.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(CommentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = "Comment deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CommentDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Comment post %s has been deleted.' % (
            self.object.post))
        return message

    def get_success_url(self, **kwargs):
        return reverse_lazy('edit_comment', args=(self.object.pk,))
