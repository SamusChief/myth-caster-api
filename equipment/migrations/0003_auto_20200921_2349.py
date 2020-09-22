# Generated by Django 3.1.1 on 2020-09-21 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0002_auto_20200920_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='weaponproperty',
            name='authorized_editors',
            field=models.ManyToManyField(blank=True, related_name='_weaponproperty_authorized_editors_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='weaponproperty',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]