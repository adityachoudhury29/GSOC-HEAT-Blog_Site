# Generated by Django 4.0.4 on 2022-07-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/'),
        ),
    ]
