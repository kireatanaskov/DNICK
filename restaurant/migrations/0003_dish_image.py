# Generated by Django 5.0.6 on 2024-05-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_employees_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dishes/'),
        ),
    ]