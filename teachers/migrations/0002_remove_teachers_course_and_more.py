# Generated by Django 5.0.6 on 2024-07-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='course',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='place_of_birth',
        ),
        migrations.AddField(
            model_name='teachers',
            name='account_number',
            field=models.PositiveBigIntegerField(default=2345),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='teacher_contact',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='years_of_experience',
            field=models.ImageField(default=5, upload_to=''),
            preserve_default=False,
        ),
    ]