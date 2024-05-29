# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    id = models.IntegerField(primary_key=True)
    gradenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    starttime = models.DateTimeField()
    roomid = models.ForeignKey('Room', models.DO_NOTHING, db_column='roomid')
    instructorid = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='instructorid')
    attendanceid = models.ForeignKey(Attendance, models.DO_NOTHING, db_column='attendanceid')
    subjectid = models.ForeignKey('Subject', models.DO_NOTHING, db_column='subjectid')
    costid = models.ForeignKey('Cost', models.DO_NOTHING, db_column='costid')

    class Meta:
        managed = False
        db_table = 'class'


class Cost(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()
    parentid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cost'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Grade(models.Model):
    id = models.IntegerField(primary_key=True)
    gradenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grade'


class Instructor(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phoneid = models.ForeignKey('Phone', models.DO_NOTHING, db_column='phoneid')
    subjectid = models.ForeignKey('Subject', models.DO_NOTHING, db_column='subjectid')

    class Meta:
        managed = False
        db_table = 'instructor'


class Parent(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')

    class Meta:
        managed = False
        db_table = 'parent'


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    phonetypeid = models.ForeignKey('Phonetype', models.DO_NOTHING, db_column='phonetypeid')
    number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Phonetype(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'phonetype'


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    roomnumber = models.IntegerField()
    capacity = models.IntegerField()
    buildinglocation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gradeid = models.ForeignKey(Grade, models.DO_NOTHING, db_column='gradeid', blank=True, null=True)
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subject'
