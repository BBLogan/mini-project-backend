# Generated by Django 5.0.3 on 2024-04-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_bad_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
