# Generated by Django 2.1.5 on 2019-01-14 21:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('attack', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('health', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cost', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('img', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Race_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rarity_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='race_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Race_card'),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Rarity_card'),
        ),
    ]
