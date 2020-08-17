from django.contrib import admin

# Register your models here.
from .models import User, Subject
from reservation.models import WorkModel, ReserveModel

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(WorkModel)
admin.site.register(ReserveModel)