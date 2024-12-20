# Generated by Django 5.0.7 on 2024-11-05 15:25

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Data Science', 'Data_Science'), ('AI&ML', 'AI&ML'), ('Graphic Design', 'Graphic Design'), ('Arts and Crafts', 'Arts and Crafts'), ('Design', 'Design'), ('Music', 'Music'), ('Electrical', 'Electrical')], max_length=20)),
                ('difficulty_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
