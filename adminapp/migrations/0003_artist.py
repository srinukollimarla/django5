# Generated by Django 4.2.5 on 2023-10-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_delete_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('male', 'male'), ('Female', 'Female'), ('other', 'other')], max_length=10)),
                ('mobile', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True)),
                ('category', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'artist_table',
            },
        ),
    ]
