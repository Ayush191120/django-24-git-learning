# Generated by Django 5.0.2 on 2024-02-23 07:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.TextField()),
            ],
            options={
                'db_table': 'celebration',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetype', models.CharField(choices=[('sick leave', 'sick leave'), ('casual leave', 'casual leave'), ('maternity leave', 'maternity leave'), ('paternity leave', 'paternity leave'), ('annual leave', 'annual leave')], max_length=100)),
                ('notes', models.CharField(max_length=100)),
                ('dates', models.CharField(max_length=100)),
                ('isapproved', models.BooleanField(default=False)),
                ('reason', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'leave',
            },
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'relationtype',
            },
        ),
        migrations.CreateModel(
            name='CelebrationParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 0), (1, 1)])),
                ('celebrationid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.celebration')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'celebrationparticipants',
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofbirth', models.DateField()),
                ('dateofjoining', models.DateField()),
                ('department', models.CharField(choices=[('administration', 'administration'), ('Research', 'Research'), ('sales', 'sales'), ('marketing', 'markrting')], max_length=100)),
                ('address', models.TextField()),
                ('emergencycontactno', models.CharField(max_length=100)),
                ('lastappraisaldate', models.DateField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userdetail',
            },
        ),
        migrations.CreateModel(
            name='UserRelative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotactnumber', models.CharField(max_length=100)),
                ('relationtypeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.relationtype')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userrelative',
            },
        ),
    ]
