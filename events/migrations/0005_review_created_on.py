# Generated by Django 4.2.3 on 2023-10-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_review_event_alter_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
