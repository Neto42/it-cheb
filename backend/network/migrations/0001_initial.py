# Generated by Django 3.2.8 on 2021-10-30 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statement', '0003_alter_statement_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passability', models.IntegerField()),
                ('place', models.CharField(max_length=25)),
                ('object_type', models.CharField(max_length=30)),
                ('statement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='statement.statement')),
            ],
        ),
        migrations.CreateModel(
            name='Rezult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rezult', models.BooleanField()),
                ('Network', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='network.network')),
            ],
        ),
    ]