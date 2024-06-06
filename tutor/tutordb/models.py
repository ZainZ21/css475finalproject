# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')
    classid = models.ForeignKey('Class', models.DO_NOTHING, db_column='classid')
    present = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'


class Class(models.Model):
    starttime = models.DateTimeField()
    roomid = models.ForeignKey('Room', models.DO_NOTHING, db_column='roomid')
    instructorid = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='instructorid')
    subjectid = models.ForeignKey('Subject', models.DO_NOTHING, db_column='subjectid')
    costid = models.ForeignKey('Cost', models.DO_NOTHING, db_column='costid')

    class Meta:
        managed = False
        db_table = 'class'
        unique_together = (('starttime', 'roomid', 'instructorid'),)


class Cost(models.Model):
    cost = models.IntegerField()
    parentid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cost'


class Grade(models.Model):
    gradeid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid', blank=True, null=True)
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classid', blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade'


class Instructor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    phoneid = models.ForeignKey('Phone', models.DO_NOTHING, db_column='phoneid')

    class Meta:
        managed = False
        db_table = 'instructor'


class Parent(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')

    class Meta:
        managed = False
        db_table = 'parent'
        unique_together = (('firstname', 'lastname', 'email'),)


class Phone(models.Model):
    phonetypeid = models.ForeignKey('Phonetype', models.DO_NOTHING, db_column='phonetypeid')
    number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Phonetype(models.Model):
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'phonetype'


class Room(models.Model):
    roomnumber = models.IntegerField()
    capacity = models.IntegerField()
    buildinglocation = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'room'


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student'


class StudentClass(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentid', primary_key=True) 
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classid')

    class Meta:
        managed = False
        db_table = 'student_class'
        unique_together = (('studentid', 'classid'),)


class Subject(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subject'

class Role(models.TextChoices):
    PARENT = 'parent'
    STAFF = 'staff'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.PARENT)