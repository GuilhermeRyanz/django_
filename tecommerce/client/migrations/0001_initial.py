# Generated by Django 5.1.1 on 2024-10-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('name', models.CharField(db_column='name', max_length=70)),
                ('age', models.IntegerField(db_column='age')),
                ('rg', models.CharField(db_column='rg', max_length=12)),
                ('cpf', models.CharField(db_column='cpf', max_length=12)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('description', models.TextField(db_column='description')),
                ('quantity', models.IntegerField(db_column='quantity', default=())),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
    ]
