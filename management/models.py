from django.db import models
from numpy import number

# Create your models here.
class Year(models.Model):
  name_year = models.CharField(max_length=20)

  def __str__(self):
    return self.name_year

class Semester(models.Model):
  name_semester = models.CharField(max_length=20)
  year = models.ForeignKey(Year, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_semester
class Week(models.Model):
  name_week = models.DateField()
  semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name_week)

class Teacher(models.Model):
  lastname = models.CharField(max_length=50)
  firstname = models.CharField(max_length=50)
  StatusChoices = models.TextChoices('type', 'professeur vacataire')
  status = models.CharField(blank=True, choices=StatusChoices.choices, max_length=20)

  def __str__(self):
    return self.lastname

class Promotion(models.Model):
  name_promotion = models.CharField(max_length=20)
  year = models.ForeignKey(Year, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_promotion

class Td(models.Model):
  name_td = models.CharField(max_length=5)
  promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_td

class Tp(models.Model):
  name_tp = models.CharField(max_length=5)
  td = models.ForeignKey(Td, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_tp

class Subject(models.Model):
  name_subject = models.CharField(max_length=20)
  number_cm_sessions = models.PositiveIntegerField(default=0)
  number_td_sessions = models.PositiveIntegerField(default=0)
  number_tp_sessions = models.PositiveIntegerField(default=0)
  promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_subject

class Sessions(models.Model):
  TypeSessionsChoices = models.TextChoices('type', 'cm td tp')
  type_sessions = models.CharField(blank=True, choices=TypeSessionsChoices.choices, max_length=20)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  number_sessions = models.PositiveIntegerField(default=0)
  promotion = models.ForeignKey(Promotion, blank=True, null=True, on_delete=models.CASCADE, related_name='promotion')
  td = models.ForeignKey(Td, blank=True, null=True, on_delete=models.CASCADE, related_name='td')
  tp = models.ManyToManyField(Tp, blank=True, related_name='tp')
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  week = models.ForeignKey(Week, on_delete=models.CASCADE)
