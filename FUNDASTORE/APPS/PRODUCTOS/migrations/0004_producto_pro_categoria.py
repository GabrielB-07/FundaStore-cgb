# Generated by Django 3.1.7 on 2021-02-22 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTOS', '0003_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='pro_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PRODUCTOS.categoria'),
        ),
    ]
