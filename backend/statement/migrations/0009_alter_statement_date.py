# Generated by Django 3.2.8 on 2021-10-30 23:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0008_alter_statement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 23, 37, 45, 767856, tzinfo=utc)),
        ),
    ]