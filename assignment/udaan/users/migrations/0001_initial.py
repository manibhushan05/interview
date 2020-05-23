# Generated by Django 3.0.6 on 2020-05-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(default='', max_length=70)),
                ('last_name', models.CharField(default='', max_length=70)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]