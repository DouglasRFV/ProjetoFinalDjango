# Generated by Django 3.1.2 on 2020-10-21 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pgto', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mensalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mensalista')),
            ],
        ),
    ]