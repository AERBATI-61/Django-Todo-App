# Generated by Django 3.2.4 on 2021-12-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_alter_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='article.Category'),
        ),
    ]
