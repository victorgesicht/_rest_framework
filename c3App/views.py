from django.shortcuts import render
from.forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from rest_framework.decorators import api_view, detail_view,List_view, staff_member_required
from django.conf import settings
import os



@detail_view(['POST'])
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = post
            comment.comment_creator = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': post.comments(),
        'comment_form': comment_form
    })


@api_view(['GET'])
def home(request):
    return render(request, 'index.html')

@List_view(['GET'])
def reports(request):
    return render(request, 'reports.html')

@staff_member_required
def orders(request):
    return render(request, 'orders.html')


@staff_member_required
def view_logs(request):
    log_path = os.path.join(settings.BASE_DIR, 'logs', 'django.log')

    #absolute path to the log file not the relative path. the difference is that
    # absolute path for example:/home/user/project/logs/django.log
    # starts from the root directory
    # while relative path starts from the current working directory example:./logs/django.log
    with open(log_path, 'r')as f:
        log_content=f.read()

    return render(request, 'view_logs.html', {'log_content':log_content})
