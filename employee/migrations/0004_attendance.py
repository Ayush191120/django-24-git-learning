# Generated by Django 5.0.2 on 2024-03-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_leave_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Pin', models.IntegerField()),
                ('Date', models.DateField()),
                ('Signin', models.TimeField()),
                ('Signout', models.TimeField()),
                ('Workinghour', models.IntegerField()),
            ],
            options={
                'db_table': 'Attendance',
            },
        ),
    ]