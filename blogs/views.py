from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostModelForm

class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

    # def queryset(self):
    #     qs = super(StudentListView, self).get_queryset()
    #     # if course_id:
    #     qs = qs.filter(published_date__lte=timezone.now())
        # return qs
# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blogs/post_list.html', {'posts': posts})

# def list_view(request):
#     reguest_course = request.GET
#     if 'course_id' in reguest_course:
#         list_students = Student.objects.filter(
#             courses=reguest_course['course_id'])
#     else:
#         list_students = Student.objects.all()
# return render(request, 'students/list.html', {'list_students':
# list_students})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Post %s has been add successfully.' % (
                post.title))
            return redirect('post_detail', post.id)
    else:
        form = PostModelForm()
    return render(request, 'blogs/post_edit.html', {'form': form})

def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form .is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Post %s has been successfully edit.' % (
                post.title))
            return redirect('post_detail', post.id)

    else:
        form = PostModelForm(instance=post)
    return render(request, 'blogs/post_edit.html', {'form': form})


#
# def detail(request, pk):
#     student = Student.objects.get(id=pk)
#     return render(request, 'students/detail.html', {'student': student})



# def detail(request, pk):
#     coaches = Coach.objects.get(id=pk)
#     context = {'coaches': coaches}

#     coach_courses = Course.objects.filter(coach=pk)
#     assistants_courses = Course.objects.filter(assistant=pk)
#     context['coach_courses'] = coach_courses
#     context['assistants_courses'] = assistants_courses
#     return render(request, 'coaches/detail.html', context)
