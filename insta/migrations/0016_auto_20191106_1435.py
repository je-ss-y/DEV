# Generated by Django 2.2.6 on 2019-11-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0015_auto_20191106_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(default='e.g Beginner, Junior, Senior', max_length=15, null=True),
        ),
    ]
