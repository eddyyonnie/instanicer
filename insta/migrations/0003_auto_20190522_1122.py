# Generated by Django 2.2.1 on 2019-05-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=400)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about',
        ),
    ]
