# Generated by Django 3.2.4 on 2021-06-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_comment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurant.order'),
        ),
    ]
