# Generated by Django 3.2.8 on 2021-10-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_network_statement'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='social',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
