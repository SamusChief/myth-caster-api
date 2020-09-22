# Generated by Django 3.1.1 on 2020-09-21 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('game_type', models.CharField(choices=[('IP', 'In Person'), ('O', 'Online'), ('IP+B', 'Both In-Person and Online')], db_index=True, max_length=4)),
                ('game_frequency', models.CharField(choices=[('W', 'Weekly'), ('BW', 'Bi-Weekly'), ('M', 'Monthly'), ('H', 'On Hold'), ('O', 'Other')], db_index=True, max_length=2)),
                ('authorized_editors', models.ManyToManyField(blank=True, related_name='_party_authorized_editors_+', to=settings.AUTH_USER_MODEL)),
                ('game_masters', models.ManyToManyField(related_name='parties_gming', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(blank=True, related_name='parties_playing', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
