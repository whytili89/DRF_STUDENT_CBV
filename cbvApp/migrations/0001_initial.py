# Generated by Django 4.0.2 on 2022-02-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
