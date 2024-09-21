from django.contrib import admin

# Register your models here.
from ai.models import Barrage
admin.site.register(Barrage)
from ai.models import Admin
admin.site.register(Admin)

from ai.models import Book
admin.site.register(Book)