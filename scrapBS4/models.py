from django.db import models
from .utils import get_link_data, get_dict_data,get_link_meta

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference= models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_difference','-created',)

    def save(self,*args,**kwargs):
        name, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff,2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0

        self.name = name
        self.current_price = price 
        super().save(*args,**kwargs)

class WordDictionary(models.Model):
    word = models.CharField(max_length=120)
    search = models.CharField(max_length=120, blank=True)
    meaning = models.CharField(max_length=500, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.word)

    class Meta:
        ordering = ('-timeStamp',)

    def save(self, *args, **kwargs):
        word, meaning = get_dict_data(self.word)
        self.search = word
        self.meaning = meaning
        super().save(*args, **kwargs)

class GenerateMeta(models.Model):
    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=160)
    keywords = models.CharField(max_length=500)
    url = models.URLField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
       ordering = ('-timeStamp',)

    def save(self, *args, **kwargs):
        title, desc, keywords = get_link_meta(self.url)
        self.title = title
        self.desc = desc
        self.keywords = keywords
        super().save(*args,**kwargs)

