# Generated by Django 4.2.7 on 2024-05-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rood_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]