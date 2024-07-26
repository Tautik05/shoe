# Generated by Django 5.0.7 on 2024-07-25 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('complete', models.IntegerField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='home.shoes')),
            ],
        ),
    ]