# Generated by Django 4.1.2 on 2022-10-20 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dijeta_je_meta', '0008_newweight_nova_tezina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newweight',
            name='current_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dijeta_je_meta.startuserweightandheight'),
        ),
        migrations.AlterField(
            model_name='newweight',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
