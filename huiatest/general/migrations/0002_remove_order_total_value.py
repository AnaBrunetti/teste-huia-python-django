# Generated by Django 3.1.4 on 2020-12-25 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_value',
        ),
    ]