# Generated by Django 2.2.3 on 2019-07-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_auto_20190721_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal',
            name='write',
            field=models.TextField(null=True),
        ),
    ]
