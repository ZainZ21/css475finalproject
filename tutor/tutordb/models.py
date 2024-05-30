from django.db import models

class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='studentid')
    class_instance = models.ForeignKey('Class', on_delete=models.CASCADE, db_column='classid')
    present = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'attendance'

class Class(models.Model):
    starttime = models.DateTimeField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, db_column='roomid')
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, db_column='instructorid')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subjectid')
    cost = models.ForeignKey('Cost', on_delete=models.CASCADE, db_column='costid')

    class Meta:
        db_table = 'class'
        unique_together = (('starttime', 'room', 'instructor'),)

class Cost(models.Model):
    cost = models.IntegerField()
    parentid = models.IntegerField()

    class Meta:
        db_table = 'cost'

class Grade(models.Model):
    gradenumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'grade'

class Instructor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE, db_column='phoneid')

    class Meta:
        db_table = 'instructor'

class Parent(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='studentid')

    class Meta:
        db_table = 'parent'
        unique_together = (('firstname', 'lastname', 'email'),)

class Phone(models.Model):
    phonetype = models.ForeignKey('Phonetype', on_delete=models.CASCADE, db_column='phonetypeid')
    number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'phone'

class Phonetype(models.Model):
    type = models.CharField(max_length=10)

    class Meta:
        db_table = 'phonetype'

class Room(models.Model):
    roomnumber = models.IntegerField()
    capacity = models.IntegerField()
    buildinglocation = models.CharField(max_length=100)

    class Meta:
        db_table = 'room'

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, db_column='gradeid', blank=True, null=True)

    class Meta:
        db_table = 'student'

class Subject(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'subject'
