# Generated by Django 5.0.6 on 2024-06-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_teacher', models.CharField(max_length=20)),
                ('class_size', models.PositiveIntegerField()),
                ('class_capacity', models.PositiveBigIntegerField()),
                ('meetings', models.CharField(max_length=20)),
                ('class_rep', models.CharField(max_length=20)),
                ('enrollment', models.PositiveSmallIntegerField()),
                ('class_goal', models.CharField(max_length=30)),
                ('class_vision', models.CharField(max_length=20)),
                ('class_id', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
