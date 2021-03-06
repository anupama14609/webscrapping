# Generated by Django 3.2.6 on 2021-08-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapBS4', '0002_alter_link_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordDictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=120)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('timeStamp',),
            },
        ),
    ]
