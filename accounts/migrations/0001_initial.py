# Generated by Django 3.0.5 on 2021-03-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('semester', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('class_name', models.CharField(max_length=20)),
            ],
        ),
    ]
