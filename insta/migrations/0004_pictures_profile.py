# Generated by Django 2.2.1 on 2019-05-22 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20190522_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
    ]
