# Generated by Django 3.0.3 on 2020-07-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='signup',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
