# Generated by Django 3.2.4 on 2021-06-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formuláriopergunta',
            name='pos',
            field=models.IntegerField(db_column='Pos', default=None, null=True, verbose_name=django.db.models.deletion.SET_NULL),
        ),
    ]
