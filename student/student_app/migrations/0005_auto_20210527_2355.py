# Generated by Django 3.2.3 on 2021-05-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_auto_20210523_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_detail',
            name='roll_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='students_detail',
            name='roll_number',
            field=models.BigIntegerField(),
        ),
    ]