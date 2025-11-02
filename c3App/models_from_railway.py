# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class C3AppBlogpost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey('C3AppDefaultuser', models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'c3App_blogpost'


class C3AppBlogpostCategory(models.Model):
    blogpost = models.ForeignKey(C3AppBlogpost, models.DO_NOTHING)
    category = models.ForeignKey('C3AppCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'c3App_blogpost_category'
        unique_together = (('blogpost', 'category'),)


class C3AppBugreports(models.Model):
    created_at = models.DateTimeField()
    reports = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    poc_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'c3App_bugreports'


class C3AppCategory(models.Model):
    categoryclass = models.CharField(db_column='categoryClass', unique=True, max_length=100)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    object_id = models.PositiveIntegerField()
    contenttype = models.ForeignKey('DjangoContentType', models.DO_NOTHING, db_column='ContentType_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c3App_category'


class C3AppDefaults(models.Model):
    logoimage = models.CharField(db_column='logoImage', max_length=100)  # Field name made lowercase.
    logoimagename = models.CharField(db_column='logoImageName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c3App_defaults'


class C3AppDefaultuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    is_active = models.BooleanField()
    role = models.CharField(max_length=20)
    is_admin = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'c3App_defaultuser'


class C3AppDefaultuserGroups(models.Model):
    defaultuser = models.ForeignKey(C3AppDefaultuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'c3App_defaultuser_groups'
        unique_together = (('defaultuser', 'group'),)


class C3AppDefaultuserUserPermissions(models.Model):
    defaultuser = models.ForeignKey(C3AppDefaultuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'c3App_defaultuser_user_permissions'
        unique_together = (('defaultuser', 'permission'),)


class C3AppLogentries(models.Model):
    logger_name = models.CharField(max_length=255)
    log_level = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'c3App_logentries'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(C3AppDefaultuser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
