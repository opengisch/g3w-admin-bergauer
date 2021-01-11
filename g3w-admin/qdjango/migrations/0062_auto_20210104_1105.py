# Generated by Django 2.2.16 on 2021-01-04 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0061_auto_20210104_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionTokenFilterLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qgs_expr', models.TextField()),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qdjango.Layer')),
                ('session_token_filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stf_layers', to='qdjango.SessionTokenFilter')),
            ],
        ),
        migrations.DeleteModel(
            name='SingleLayerSessionFilter',
        ),
    ]