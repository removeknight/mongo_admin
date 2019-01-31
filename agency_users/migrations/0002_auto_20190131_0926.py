# Generated by Django 2.0.7 on 2019-01-31 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='license',
        ),
        migrations.AlterField(
            model_name='user',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agency_users.Agency'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]