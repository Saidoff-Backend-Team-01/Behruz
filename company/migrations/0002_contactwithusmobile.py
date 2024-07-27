# Generated by Django 5.0.6 on 2024-07-27 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactWithUsMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Contact With Us',
                'verbose_name_plural': 'Contact With Us',
            },
        ),
    ]
