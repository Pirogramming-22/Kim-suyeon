# Generated by Django 4.2.17 on 2025-01-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0008_remove_post_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
