# Generated by Django 3.2.4 on 2021-12-13 09:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20211213_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
