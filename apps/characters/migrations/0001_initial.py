# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField()),
                ('strModifier', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('dexModifier', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('conModifier', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('intModifier', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('wisModifier', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('chaModifier', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('my_class', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('background', models.CharField(max_length=50)),
                ('alignment', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_characters', to='logreg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_equipment', to='characters.Character')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='characters.Character'),
        ),
    ]
