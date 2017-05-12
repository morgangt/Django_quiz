# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-11 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('model', models.CharField(max_length=200)),
                ('cat', models.CharField(choices=[('A', '\u041c\u043e\u0442\u043e\u0446\u0438\u043a\u043b'), ('B', '\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c'), ('C', '\u0413\u0440\u0443\u0437\u043e\u0432\u0438\u043a'), ('D', '\u0410\u0432\u0442\u043e\u0431\u0443\u0441'), ('BE', '\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c \u0441 \u043f\u0440\u0438\u0446\u0435\u043f\u043e\u043c'), ('CE', '\u0413\u0440\u0443\u0437\u043e\u0432\u0438\u043a \u0441 \u043f\u0440\u0438\u0446\u0435\u043f\u043e\u043c'), ('DE', '\u0410\u0432\u0442\u043e\u0431\u0443\u0441 \u0441 \u043f\u0440\u0438\u0446\u0435\u043f\u043e\u043c')], default='B', max_length=2)),
            ],
        ),
    ]