# Generated by Django 4.1.3 on 2022-11-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_individualentrepreneur_cluster_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='IECluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INN', models.BigIntegerField()),
                ('cluster_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='cluster_id',
        ),
    ]
