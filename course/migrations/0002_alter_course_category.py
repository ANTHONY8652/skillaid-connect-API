# Generated by Django 5.0.7 on 2024-11-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('Programming', 'Programming'), ('Data Science', 'Data_Science'), ('AI&ML', 'AI&ML'), ('Graphic Design', 'Graphic Design'), ('Arts and Crafts', 'Arts and Crafts'), ('Design', 'Design'), ('Music', 'Music'), ('Electrical', 'Electrical'), ('Physical', 'Physical')], max_length=30),
        ),
    ]
