# Generated by Django 2.2.2 on 2019-06-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20190616_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(primary_key=True, serialize=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('projects', models.ManyToManyField(to='projects.Project', verbose_name='Related Projects')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]