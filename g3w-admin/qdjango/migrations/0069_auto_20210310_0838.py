# Generated by Django 2.2.16 on 2021-03-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0068_project_autozoom_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlelayerconstraint',
            name='for_editing',
            field=models.BooleanField(default=False, help_text='Active this constraint for users have editing grant on layer/project', null=True, verbose_name='Active for editing'),
        ),
        migrations.AddField(
            model_name='singlelayerconstraint',
            name='for_view',
            field=models.BooleanField(default=False, help_text='Active this constraint for users have viewing grant on layer/project', null=True, verbose_name='Active for visualization'),
        ),

        # Following SQL update statement is for G3W-SUITE installations without constraints split context.
        migrations.RunSQL(
            "UPDATE qdjango_singlelayerconstraint set for_view=true"
        ),
    ]