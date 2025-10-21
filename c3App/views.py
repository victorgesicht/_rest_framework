from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import blogPost
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import os
from django.http import HttpResponse


@require_http_methods(['GET', 'POST'])
def post_detail_view(request, pk):
    post = get_object_or_404(blogPost, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = blogPost
            comment.comment_creator = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': blogPost,
        'comments': blogPost.comments.all() if hasattr(blogPost, 'comments') else [],
        'comment_form': comment_form
    })


def home(request):
    return HttpResponse("gusyffusgfu")

@require_GET
def reports(request):
    return render(request, 'reports.html')


def orders(request):
    return render(request, 'orders.html')