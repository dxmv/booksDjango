# Generated by Django 3.2.4 on 2021-06-26 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210626_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(db_constraint=False, default=False, on_delete=django.db.models.deletion.CASCADE, to='book.genre'),
        ),
    ]
