# Generated by Django 3.2.2 on 2021-05-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='catego',
            field=models.CharField(choices=[('E', 'Electronics'), ('F', 'Fashion')], default='', max_length=3),
        ),
    ]