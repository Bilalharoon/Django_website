# Generated by Django 2.0.2 on 2018-04-16 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('stars', models.DecimalField(decimal_places=1, max_digits=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Products')),
            ],
        ),
    ]