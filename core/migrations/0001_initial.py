# Generated by Django 2.2 on 2019-05-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=22)),
                ('email', models.TextField()),
            ],
        ),
    ]
