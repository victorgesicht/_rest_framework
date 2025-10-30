from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("...not without a valid email.")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.is_active = kwargs.get('is_active', True)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs.get('is_superuser'):
            raise ValueError("Try BruteForcing son")
        if not kwargs.get('is_staff'):
            raise ValueError("Try BruteForcing son")


        return self.create_user(email, password, **kwargs)

class DefaultUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, default='DefaultUser')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class BugReports(models.Model):
    reports=models.CharField(max_length=300, default=' whatchu learning...?',)
    title=models.CharField(max_length=100, default='titleHead')
    poc_image=models.ImageField(upload_to='bug_pics/', default='nopic.jpg')
    created_at=models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True, default='slug')
    body=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category',blank=True, related_name='categoryClass')


    def __str__(self):
        return self.title

class Category(models.Model):
    categoryClass = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    ContentType= models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField ()
    content_object = GenericForeignKey('ContentType', 'object_id')

    def __str__(self):
        return self.categoryClass

class LogEntries(models.Model):
    logger_name = models.CharField(max_length=255)
    log_level = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.log_level} - {self.logger_name}: {self.message}"

class Defaults(models.Model):
    logoImage = models.ImageField('samurai.jpeg', upload_to='default_images/', default='samurai.jpeg')
    logoImageName = models.CharField(max_length=100, default='samurai.jpeg')
    def __str__(self):
        return self.logoImageName

