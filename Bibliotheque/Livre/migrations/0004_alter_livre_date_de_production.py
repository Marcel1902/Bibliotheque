# Generated by Django 4.2.7 on 2023-12-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livre', '0003_alter_livre_date_de_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='Date_de_production',
            field=models.DateField(blank=True),
        ),
    ]
