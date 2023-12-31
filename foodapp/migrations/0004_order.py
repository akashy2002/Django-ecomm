# Generated by Django 4.1.7 on 2023-06-13 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodapp', '0003_fooditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default=0, null=True)),
                ('price', models.BigIntegerField(blank=True, default=0, null=True)),
                ('quantity', models.BigIntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.fooditem')),
            ],
        ),
    ]
