# Generated by Django 3.0.4 on 2020-06-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('font', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'classification',
            },
        ),
    ]
