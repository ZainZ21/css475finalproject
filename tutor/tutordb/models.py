from django.db import models


class Attendance(models.Model):
    gradenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance'


class Class(models.Model):
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
    cost = models.IntegerField()
    parentid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cost'


class Grade(models.Model):
    gradenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grade'


class Instructor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
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
    gradeid = models.ForeignKey(Grade, models.DO_NOTHING, db_column='gradeid', blank=True, null=True)
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'subject'
