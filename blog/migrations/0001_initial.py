# Generated by Django 4.0 on 2022-03-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('ltext', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
