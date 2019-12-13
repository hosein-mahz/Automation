# Generated by Django 2.2 on 2019-12-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0002_auto_20191213_1436'),
        ('Services', '0001_initial'),
        ('physicing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280)),
                ('data', models.DateTimeField(auto_now=True)),
                ('patient_id', models.ForeignKey(null=True, on_delete=True, to='patient.Patient')),
                ('physician_id', models.ForeignKey(null=True, on_delete=True, to='physicing.physician')),
            ],
        ),
        migrations.CreateModel(
            name='Service_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
                ('service_id', models.ForeignKey(null=True, on_delete=True, to='Services.Services')),
            ],
        ),
        migrations.CreateModel(
            name='Medecine_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.CharField(max_length=150)),
                ('qty', models.IntegerField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
        migrations.CreateModel(
            name='Hoteling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(choices=[(1, '1-2'), (2, '2-4')])),
                ('qty', models.IntegerField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
        migrations.CreateModel(
            name='device_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280)),
                ('qty', models.IntegerField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
        migrations.CreateModel(
            name='Classtreatment_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.TextField()),
                ('description', models.TextField()),
                ('Operation_record_id', models.ForeignKey(null=True, on_delete=True, to='ParaClininical.Operation_record')),
            ],
        ),
    ]