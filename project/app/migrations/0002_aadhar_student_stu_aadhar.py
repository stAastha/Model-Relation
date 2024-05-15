# Generated by Django 5.0.4 on 2024-04-04 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='stu_aadhar',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.aadhar'),
            preserve_default=False,
        ),
    ]
