# Generated by Django 5.0.3 on 2024-04-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_bad_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='bad_feedback',
            field=models.TextField(default=False, max_length=800),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='good_feedback',
            field=models.TextField(default=False, max_length=800),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='other_feedback',
            field=models.TextField(default=False, max_length=800),
        ),
    ]
