# Generated by Django 3.1.14 on 2024-07-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsAndLogin', '0003_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
