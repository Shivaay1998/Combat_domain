# Generated by Django 4.0.4 on 2022-12-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combatapp', '0012_alter_entry_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='profile_img',
            field=models.ImageField(default='', upload_to='pics/images'),
        ),
    ]
