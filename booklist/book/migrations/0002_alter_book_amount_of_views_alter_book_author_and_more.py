# Generated by Django 4.2.4 on 2023-09-02 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amount_of_views',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
