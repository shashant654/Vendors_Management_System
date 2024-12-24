# Generated by Django 5.0.3 on 2024-12-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='services_offered',
        ),
        migrations.AddField(
            model_name='vendor',
            name='services_offered',
            field=models.CharField(choices=[('it_services', 'It Services'), ('logistics', 'Logistics')], default='logistics', max_length=20),
        ),
    ]