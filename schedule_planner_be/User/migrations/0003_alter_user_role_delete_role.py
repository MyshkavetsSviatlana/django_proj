# Generated by Django 4.1 on 2022-08-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_role_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SuperAdmin', 'SuperAdmin'), ('Administrator', 'Administrator'), ('Manager', 'Manager'), ('Teacher', 'Teacher')], max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]