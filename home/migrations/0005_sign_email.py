# Generated by Django 3.2.5 on 2021-08-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_signup_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='email',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]