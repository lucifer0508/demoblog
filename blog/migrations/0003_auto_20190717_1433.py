# Generated by Django 2.2.3 on 2019-07-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='email',
            field=models.CharField(default='Empty...', max_length=40),
        ),
    ]
