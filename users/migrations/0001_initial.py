# Generated by Django 4.1.2 on 2022-11-02 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(max_length=25)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenderIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_identity', models.CharField(max_length=25)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SexualOrientation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexual_orientation', models.CharField(max_length=25)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('profile_photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_photos')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('ethnicity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.ethnicity')),
                ('gender_identity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.genderidentity')),
                ('sexual_orientation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.sexualorientation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
