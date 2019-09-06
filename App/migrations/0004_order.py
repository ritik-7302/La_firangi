# Generated by Django 2.0.5 on 2019-08-13 18:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0003_auto_20190811_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('order_product', models.ForeignKey(default=None, on_delete='CASCADE', to='App.Product')),
                ('order_user', models.ForeignKey(default=None, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]