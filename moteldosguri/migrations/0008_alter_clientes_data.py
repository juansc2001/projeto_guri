# Generated by Django 4.2.19 on 2025-02-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moteldosguri', '0007_alter_clientes_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='data',
            field=models.DateField(default='2012-12-12'),
        ),
    ]
