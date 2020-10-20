# Generated by Django 3.1.2 on 2020-10-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0150_auto_20200723_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategory',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Attiva fino al'),
        ),
        migrations.AddField(
            model_name='ticketcategory',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Attiva dal'),
        ),
    ]
