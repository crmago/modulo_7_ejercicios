# Generated by Django 5.0.6 on 2024-06-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id',
        ),
        migrations.AlterField(
            model_name='curso',
            name='cod',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
