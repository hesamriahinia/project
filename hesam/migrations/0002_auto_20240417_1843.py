# Generated by Django 3.2.25 on 2024-04-17 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hesam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('created_date',)},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]
