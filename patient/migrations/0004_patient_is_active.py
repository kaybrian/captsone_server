# Generated by Django 5.1.6 on 2025-03-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_healthvital_exang_alter_healthvital_rest_ecg'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
