from django.contrib import admin
from .models import DefaultUser, BlogPost, BugReports, Defaults, Category

admin.site.register(DefaultUser)
admin.site.register(BlogPost)
admin.site.register(BugReports)
admin.site.register(Defaults)
admin.site.register(Category)
