# Generated by Django 5.0.2 on 2024-02-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_tasks_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
