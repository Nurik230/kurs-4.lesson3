# Generated by Django 4.2.6 on 2023-10-20 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mono', '0004_alter_post_options_alter_post_cost_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Mobile',
        ),
        migrations.AlterModelOptions(
            name='mobile',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефон'},
        ),
    ]