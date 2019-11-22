# Generated by Django 2.2.6 on 2019-11-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_make',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='on_stock',
            field=models.IntegerField(default=1),
        ),
    ]
