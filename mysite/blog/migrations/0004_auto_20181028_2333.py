# Generated by Django 2.0.5 on 2018-10-29 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181028_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comments',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 6, 33, 1, 122749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 6, 33, 1, 121750, tzinfo=utc)),
        ),
    ]
