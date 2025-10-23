from django.contrib import admin
from .models import Supporter, UserProfile, BlogPost, BugReports

admin.site.register(Supporter)
admin.site.register(UserProfile)
admin.site.register(BlogPost)
admin.site.register(BugReports)
