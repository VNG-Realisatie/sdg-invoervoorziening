# Generated by Django 2.2.24 on 2021-11-18 13:59

from django.db import migrations


def update_product_aanwezig(apps, schema_editor):
    Product = apps.get_model("producten", "Product")
    for obj in Product.objects.filter(beschikbaar=True):
        obj.product_aanwezig = True
        obj.product_aanwezig_toelichting = "Toelichting"
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("producten", "0013_auto_20211118_1201"),
    ]

    operations = [
        migrations.RunPython(update_product_aanwezig, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="product",
            name="beschikbaar",
        ),
    ]
