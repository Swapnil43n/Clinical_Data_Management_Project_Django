# Generated by Django 4.1.1 on 2023-05-04 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='clinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(choices=[('hw', 'Height/Weight'), ('bp', 'Blood Presure'), ('heartrate', 'Heart Rate')], max_length=20)),
                ('componetValue', models.CharField(max_length=20)),
                ('measuredDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalApp.patients')),
            ],
        ),
    ]
