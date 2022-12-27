# Generated by Django 4.0.4 on 2022-12-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='entry',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]