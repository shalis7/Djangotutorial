# Generated by Django 5.1.3 on 2024-11-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_asset_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(blank=True, choices=[('NA', 'Not Available'), ('AV', 'Available'), ('IU', 'In Use')], max_length=2, null=True),
        ),
    ]