from django.contrib import admin
from .models import DefaultUser, BlogPost, BugReports

admin.site.register(DefaultUser)
admin.site.register(BlogPost)
admin.site.register(BugReports)
