# Generated by Django 3.1.7 on 2021-04-18 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20210417_1735'),
        ('core', '0002_auto_20210418_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='from_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notf_from_profile', to='chat.profile'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='to_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notf_to_profile', to='chat.profile'),
        ),
    ]
