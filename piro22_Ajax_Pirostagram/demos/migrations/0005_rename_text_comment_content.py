# Generated by Django 4.2.18 on 2025-01-20 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
    ]
