<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-11-17 16:23
=======
# Generated by Django 4.1.3 on 2022-11-16 21:54
>>>>>>> main

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
<<<<<<< HEAD
            name='Author',
=======
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
>>>>>>> main
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('profile_img_url', models.URLField(blank=True, max_length=300)),
<<<<<<< HEAD
=======
                ('created_on', models.DateTimeField(auto_now_add=True)),
>>>>>>> main
                ('active', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]