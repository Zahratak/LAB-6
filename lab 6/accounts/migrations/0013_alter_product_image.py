# Generated by Django 4.1.7 on 2023-05-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_remove_customer_profile_pic_remove_product_tag_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        )
    ]
