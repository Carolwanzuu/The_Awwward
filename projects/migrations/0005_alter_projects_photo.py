# Generated by Django 3.2.5 on 2021-07-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210719_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='photo',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
