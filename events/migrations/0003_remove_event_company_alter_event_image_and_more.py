# Generated by Django 4.2.2 on 2023-08-04 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('events', '0002_alter_event_company_alter_event_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='company',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='static/uploads/events'),
        ),
        migrations.AlterField(
            model_name='event',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.mentor'),
        ),
    ]
