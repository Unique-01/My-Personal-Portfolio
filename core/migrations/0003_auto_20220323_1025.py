# Generated by Django 3.2.12 on 2022-03-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tech_used',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
