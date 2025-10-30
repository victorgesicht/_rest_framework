from django.contrib import admin
from .models import DefaultUser, BlogPost, BugReports, Defaults

admin.site.register(DefaultUser)
admin.site.register(BlogPost)
admin.site.register(BugReports)
admin.site.register(Defaults)
