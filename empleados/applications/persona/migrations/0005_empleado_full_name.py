# Generated by Django 3.2.3 on 2021-06-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Full name'),
        ),
    ]