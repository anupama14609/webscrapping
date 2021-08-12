from django.contrib import admin
from .models import Link, WordDictionary,GenerateMeta

# Register your models here.
admin.site.register((Link,WordDictionary,GenerateMeta))
