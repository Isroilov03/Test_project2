# Generated by Django 4.2 on 2023-08-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('yosh', models.IntegerField()),
                ('t_yil', models.DateField()),
                ('created', models.TimeField()),
            ],
        ),
    ]
