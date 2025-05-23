# Generated by Django 5.1 on 2024-08-10 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tipo',
            },
        ),
        migrations.AlterField(
            model_name='unidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='CabeceraVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaventa', models.DateTimeField()),
                ('nrodoc', models.CharField(max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.cliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.tipo')),
            ],
            options={
                'db_table': 'cabeceraventas',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('iddetalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='VentasApp.cabeceraventa')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasApp.producto')),
            ],
            options={
                'db_table': 'detalleventa',
            },
        ),
    ]
