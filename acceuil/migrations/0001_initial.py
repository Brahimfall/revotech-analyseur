# Generated by Django 5.0.2 on 2024-03-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]