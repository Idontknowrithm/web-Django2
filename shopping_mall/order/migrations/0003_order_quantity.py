# Generated by Django 2.2.4 on 2021-07-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210724_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default='0', verbose_name='수량'),
        ),
    ]
