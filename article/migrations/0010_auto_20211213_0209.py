# Generated by Django 3.2.4 on 2021-12-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]