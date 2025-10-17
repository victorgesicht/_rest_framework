from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType



class UserManager(BaseUserManager):
    def create_user(self,
                    email,
                    password=None,
                    **kwargs
                    ):
        if not email:
            raise ValueError(
                "...not without a valid email."
                )
        email=self.normalize_email(email)
        user=self.model(
            email=email,
            **kwargs
            )
        user.set_password(password)#check more customization options
        user.save(using=self._db)#consider env variables
        return user




    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_admin', True)

        if not kwargs.get('is_staff'):
            raise ValueError("I do not know you.")
        if not kwargs.get('is_admin'):
            raise ValueError("You are not the boss of me.")


class supporter(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, default='user')
    is_admin = models.BooleanField(default=False)
    alias=models.CharField(max_length=25, default='guest')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500, default='')
    profile_pic=models.ImageField(upload_to='profile_pics/', default='default.jpg')



class bugReports(models.Model):
    author=models.ForeignKey(UserProfile, on_delete=models.PROTECT),
    reports=models.CharField(max_length=300, default=' whatchu learning...?',)
    title=models.CharField(max_length=100, default='titleHead')
    poc_image=models.ImageField(upload_to='bug_pics/', default='nopic.jpg')
    created_at=models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.title

class blogPost(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    comments=GenericRelation('Comment')
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_creator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.comment_creator
