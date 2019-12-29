# Generated by Django 2.2 on 2019-12-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParaClininical', '0002_auto_20191221_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtreatment_order',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='classtreatment_order', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='consumable_order',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='consumable_order', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='device_order',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='device_order', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='hoteling',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='hoteling', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='medecine_order',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='medecine_order', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='operation_record',
            name='physician_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='Operation_record', to='physicing.physician'),
        ),
        migrations.AlterField(
            model_name='service_list',
            name='Operation_record_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='service_list', to='ParaClininical.Operation_record'),
        ),
        migrations.AlterField(
            model_name='service_list',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=True, related_name='service_list', to='Services.Services'),
        ),
    ]