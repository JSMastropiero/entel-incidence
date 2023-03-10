# Generated by Django 4.1.7 on 2023-03-02 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidence',
            options={'verbose_name': 'incidence', 'verbose_name_plural': 'incidences'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'place', 'verbose_name_plural': 'places'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'status', 'verbose_name_plural': 'status'},
        ),
        migrations.AlterModelOptions(
            name='statuschangelog',
            options={'verbose_name': 'status change log', 'verbose_name_plural': 'status change log'},
        ),
        migrations.AlterModelOptions(
            name='typeofstatus',
            options={'verbose_name': 'type of status', 'verbose_name_plural': 'type of status'},
        ),
        migrations.AddField(
            model_name='incidence',
            name='place',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.place'),
        ),
        migrations.AddField(
            model_name='incidence',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
    ]
