# Generated by Django 4.1.7 on 2023-02-23 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0003_scope_direct_cost_scope_equipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='project',
        ),
        migrations.AddField(
            model_name='scope',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='estimate.project'),
        ),
    ]