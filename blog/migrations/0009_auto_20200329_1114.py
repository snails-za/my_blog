# Generated by Django 2.0.6 on 2020-03-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200329_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.ImageField(default='head/user.png', max_length=200, upload_to='head/%Y/%m', verbose_name='用户头像'),
        ),
    ]
