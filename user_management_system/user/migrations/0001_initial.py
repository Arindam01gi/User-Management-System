# Generated by Django 5.0.2 on 2024-02-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField()),
                ('created_on', models.DateTimeField(null=True)),
                ('updated_on', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]