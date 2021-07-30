# Generated by Django 3.0.3 on 2021-06-18 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadingdate', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=30)),
                ('notesfile', models.FileField(upload_to='')),
                ('filetype', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]