# Generated by Django 3.2.8 on 2021-10-30 20:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_user', models.EmailField(max_length=50)),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской', max_length=10)),
                ('age', models.IntegerField()),
                ('complaint', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 20, 49, 48, 793152, tzinfo=utc))),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='city.city')),
                ('social', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='city.socialstatuses')),
            ],
        ),
    ]
