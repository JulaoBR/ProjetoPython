# Generated by Django 2.1 on 2018-08-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacaoWeb', '0003_auto_20180827_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacaoWeb.Grupo'),
        ),
    ]
