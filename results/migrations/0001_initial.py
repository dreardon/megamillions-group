# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-20 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgreementPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodName', models.CharField(default=0, max_length=14)),
                ('agreementFile', models.FileField(blank=True, null=True, upload_to='attachments')),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Agreement Periods',
            },
        ),
        migrations.CreateModel(
            name='MegaNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(default=0, max_length=14)),
                ('megaBall', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaidOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prizeAmount', models.IntegerField(default=0)),
                ('agreementPeriod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.AgreementPeriod')),
            ],
            options={
                'verbose_name_plural': 'Paid Out',
            },
        ),
        migrations.CreateModel(
            name='PrizesWon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupPrizeAmount', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Prizes Won',
            },
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('meganumbers_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.MegaNumbers')),
                ('multiplier', models.IntegerField()),
                ('drawingDate', models.DateField()),
            ],
            bases=('results.meganumbers',),
        ),
        migrations.CreateModel(
            name='GroupTicket',
            fields=[
                ('meganumbers_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.MegaNumbers')),
                ('autoPick', models.BooleanField()),
                ('agreementPeriod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='results.AgreementPeriod')),
            ],
            options={
                'verbose_name_plural': 'Group Tickets',
            },
            bases=('results.meganumbers',),
        ),
        migrations.AddField(
            model_name='prizeswon',
            name='drawing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Drawing'),
        ),
        migrations.AddField(
            model_name='prizeswon',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.GroupTicket'),
        ),
    ]
