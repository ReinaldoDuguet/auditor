# Generated by Django 4.0.1 on 2024-03-29 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuenta',
            new_name='CuentaHija',
        ),
        migrations.CreateModel(
            name='CuentaPadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cuenta', models.CharField(max_length=50)),
                ('nombre_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        migrations.AlterField(
            model_name='cuentahija',
            name='nombre_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cuentapadre'),
        ),
    ]
