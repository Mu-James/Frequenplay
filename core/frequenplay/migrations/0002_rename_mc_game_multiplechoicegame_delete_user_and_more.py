# Generated by Django 5.0 on 2023-12-31 01:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequenplay', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MC_Game',
            new_name='MultipleChoiceGame',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='multiplechoicegame',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
