# Generated by Django 2.0.2 on 2018-02-23 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0003_auto_20180223_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='entity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SRP.Entity'),
            preserve_default=False,
        ),
    ]
