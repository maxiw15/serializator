# Generated by Django 3.1.2 on 2023-02-23 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='project',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurements.sensor'),
            preserve_default=False,
        ),
    ]