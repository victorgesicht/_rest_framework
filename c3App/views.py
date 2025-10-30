from django.shortcuts import render, redirect, get_object_or_404

from .models import BlogPost, Defaults, Category
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.conf import settings
import os
from django.http import HttpResponse



def home(request):
    blogs= BlogPost.objects.all()
    default=Defaults.objects.first()  # Assuming you want the first Defaults object
    return render(request, 'index.html', {'blogs': blogs, 'default': default})


@require_GET
def reports(request):
    return render(request, 'reports.html')


def orders(request):
    return render(request, 'orders.html')