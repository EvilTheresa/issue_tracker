# Generated by Django 5.0.6 on 2024-07-10 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_task_options_remove_task_type_alter_task_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='types',
            new_name='type',
        ),
        migrations.AlterModelTable(
            name='task',
            table=None,
        ),
    ]
