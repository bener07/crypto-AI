# Generated by Django 3.2.13 on 2022-05-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_coins_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'test_model',
                'verbose_name_plural': 'test_models',
            },
        ),
    ]