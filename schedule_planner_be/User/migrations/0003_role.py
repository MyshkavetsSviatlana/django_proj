from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('SuperAdmin', 'SuperAdmin'), ('Administrator', 'Administrator'), ('Manager', 'Manager'), ('Teacher', 'Teacher')], max_length=15)),
            ],
        ),
    ]
