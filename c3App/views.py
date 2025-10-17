from django.shortcuts import render
from.forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from rest_framework.decorators import api_view, detail_view

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