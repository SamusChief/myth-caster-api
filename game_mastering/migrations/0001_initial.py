# Generated by Django 3.0.10 on 2020-09-26 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import game_mastering.models.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameMasterFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='game_master_materials/%Y/%m/%d/')),
                ('authorized_editors', models.ManyToManyField(blank=True, related_name='_file_authorized_editors_+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('authorized_editors', models.ManyToManyField(blank=True, related_name='_notes_authorized_editors_+', to=settings.AUTH_USER_MODEL)),
                ('files', models.ManyToManyField(blank=True, related_name='file_notes', to='game_mastering.GameMasterFile')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parties', models.ManyToManyField(blank=True, related_name='party_notes', to='parties.Party')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, game_mastering.models.mixins.PartiesUsersMixin),
        ),
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('secret_content', models.TextField(blank=True, null=True)),
                ('authorized_editors', models.ManyToManyField(blank=True, related_name='_handout_authorized_editors_+', to=settings.AUTH_USER_MODEL)),
                ('files', models.ManyToManyField(blank=True, related_name='file_handouts', to='game_mastering.GameMasterFile')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parties', models.ManyToManyField(blank=True, related_name='party_handouts', to='parties.Party')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, game_mastering.models.mixins.PartiesUsersMixin),
        ),
    ]