# Generated by Django 2.2.7 on 2022-06-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcomeHeader', models.CharField(max_length=1000)),
                ('welcomeParagraph', models.CharField(max_length=10000)),
            ],
        ),
    ]
