# Generated by Django 4.1.7 on 2023-03-01 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_tag_product_tags_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tags',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
