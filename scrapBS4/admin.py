from django.contrib import admin
from .models import Link, WordDictionary

# Register your models here.
admin.site.register((Link,WordDictionary))
