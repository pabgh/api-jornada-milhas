# Generated by Django 4.2.3 on 2023-07-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('autor', models.CharField(blank=True, max_length=75, null=True)),
            ],
        ),
    ]
