# Generated by Django 2.1.7 on 2020-11-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
