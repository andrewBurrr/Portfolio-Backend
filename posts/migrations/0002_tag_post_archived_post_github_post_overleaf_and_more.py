# Generated by Django 4.1.6 on 2023-02-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='overleaf',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]
