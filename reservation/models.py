from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class WorkModel(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    workdate = models.DateField(auto_now=False, auto_now_add=False)
    class TimeTable(models.TextChoices):
        c1 = 'c1', _('14:00')
        c2 = 'c2', _('15:00')
        c3 = 'c3', _('16:00')
        c4 = 'c4', _('17:00')
        c5 = 'c5', _('18:00')
        c6 = 'c6', _('19:00')
        c7 = 'c7', _('20:00')
        c8 = 'c8', _('21:00')
        c9 = 'c9', _('22:00')
    worktime = models.TextField(max_length=10, choices=TimeTable.choices, default=TimeTable.c5)

class ReserveModel(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    studentid = models.IntegerField()
    student = models.CharField(max_length=50)
    class Subject(models.TextChoices):
        sj = 'sj', _('中受国語')
        sm = 'sm', _('中受算数')
        ce = 'ce', _('中学英語')
        cm = 'cm', _('中学数学')
        kk = 'kk', _('高校古文')
        kg = 'kg', _('高校現代文')
        m1 = 'm1', _('高校数学I')
        ma = 'ma', _('高校数学A')
        m2 = 'm2', _('高校数学II')
        mb = 'mb', _('高校数学B')
        ke = 'ke', _('高校英語')
    subject = models.CharField(max_length=10, choices=Subject.choices, default=Subject.cm,null=True, blank=True)
    textbook = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    reservedate = models.DateField(auto_now=False, auto_now_add=False)
    class TimeTable(models.TextChoices):
        c1 = 'c1', _('14:00')
        c2 = 'c2', _('15:00')
        c3 = 'c3', _('16:00')
        c4 = 'c4', _('17:00')
        c5 = 'c5', _('18:00')
        c6 = 'c6', _('19:00')
        c7 = 'c7', _('20:00')
        c8 = 'c8', _('21:00')
        c9 = 'c9', _('22:00')
    reservetime = models.TextField(max_length=10, choices=TimeTable.choices)