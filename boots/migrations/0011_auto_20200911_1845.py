# Generated by Django 3.0.8 on 2020-09-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0010_auto_20200911_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='boot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='boots.Boot'),
        ),
    ]
