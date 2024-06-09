# Generated by Django 5.0.3 on 2024-06-08 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type', models.CharField(choices=[('1', 'Same Day Delivery'), ('2', 'Next Day Delivery')], max_length=100)),
                ('cake_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('cake_size', models.CharField(choices=[('1', 'Small(1kg)'), ('2', 'Medium(1.5kg)'), ('3', 'Large(2kg)')], max_length=100)),
                ('image', models.ImageField(upload_to='cake_items/images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
