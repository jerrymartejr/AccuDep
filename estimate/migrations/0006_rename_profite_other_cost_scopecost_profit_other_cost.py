# Generated by Django 4.1.7 on 2023-02-23 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0005_remove_scope_direct_cost_remove_scope_equipment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopecost',
            old_name='profite_other_cost',
            new_name='profit_other_cost',
        ),
    ]
