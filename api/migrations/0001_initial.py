# Generated by Django 5.0.4 on 2024-04-20 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('compt', models.CharField(max_length=300)),
                ('status', models.CharField(default='registered', max_length=10)),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
