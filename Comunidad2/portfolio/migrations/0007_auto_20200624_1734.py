# Generated by Django 3.0.4 on 2020-06-24 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200624_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'dd', 'verbose_name_plural': 'dd'},
        ),
    ]
