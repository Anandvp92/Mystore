# Generated by Django 5.0 on 2024-01-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_alter_customusermodel_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phonenumber',
            field=models.CharField(max_length=13, unique=True, verbose_name='Phone Number'),
        ),
    ]