from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Subject(models.Model):
    class Kamoku(models.TextChoices):
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
    subject = models.CharField(max_length=10, choices=Kamoku.choices, default=Kamoku.cm,null=True, blank=True)
    
    def __str__(self):
        return self.subject

class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    class Gender(models.IntegerChoices):
        man = 1
        woman = 2
        other = 3
    gender = models.IntegerField(choices=Gender.choices, blank=True, null=True)

    class Role(models.IntegerChoices):
        teacher = 1
        student = 2
    role = models.IntegerField(choices=Role.choices, blank=True, null=True)


    class Grade(models.TextChoices):
        shou4 = 's4', _('小学4年生')
        shou5 = 's5', _('小学5年生')
        shou6 = 's6', _('小学6年生')
        chu1 = 'c1', _('中学1年生')
        chu2 = 'c2', _('中学2年生')
        chu3 = 'c3', _('中学3年生')
        kou1 = 'k1', _('高校1年生')
        kou2 = 'k2', _('高校2年生')
        kou3 = 'k3', _('高校3年生')
    grade = models.TextField(max_length=10, choices=Grade.choices, blank=True, null=True)
    
    kamoku = models.ManyToManyField(Subject, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.role==1:
            return self.last_name + self.first_name
        else:
            return '選択できません'