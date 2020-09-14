# Generated by Django 3.1.1 on 2020-09-13 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(db_index=True, default='2020-09-13 23:59:02.295055+00:00', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
