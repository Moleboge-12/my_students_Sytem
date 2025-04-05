# Generated by Django 5.1.7 on 2025-03-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('academic_year', models.CharField(max_length=20)),
                ('wellness_status', models.CharField(choices=[('Healthy', 'Healthy'), ('In Need', 'In Need')], max_length=50)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
            ],
        ),
    ]
