# Generated by Django 2.2.18 on 2022-01-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0085_columnacl'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='has_column_acl',
            field=models.BooleanField(default=False, editable=False, verbose_name='Has column ACL constraints'),
        ),
    ]
