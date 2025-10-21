from django.contrib import admin
from .models import supporter, UserProfile, blogPost, bugReports

admin.site.register(supporter)
admin.site.register(UserProfile)
admin.site.register(blogPost)
admin.site.register(bugReports)
