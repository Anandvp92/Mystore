# Generated by Django 5.0 on 2024-01-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='phonenumber',
            field=models.CharField(max_length=13, unique=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/', verbose_name='Profile Pic'),
        ),
    ]