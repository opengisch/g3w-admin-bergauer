# Generated by Django 2.2.27 on 2022-05-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0098_auto_20220426_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_ro',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ur_ro',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Public title'),
        ),
    ]