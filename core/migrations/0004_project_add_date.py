# Generated by Django 3.2.12 on 2022-05-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220323_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
