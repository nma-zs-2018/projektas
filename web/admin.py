from django.contrib import admin

# Register your models here.
from web.models import Student

admin.site.register(Student)

from web.models import Question

admin.site.register(Question)