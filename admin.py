from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Tag, Post

class MyModelAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminMartorWidget},
	}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, MyModelAdmin)
