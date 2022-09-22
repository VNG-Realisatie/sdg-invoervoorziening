# Generated by Django 3.2.13 on 2022-09-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producten", "0036_alter_localizedgeneriekproduct_generieke_tekst"),
    ]

    operations = [
        migrations.AddField(
            model_name="localizedproduct",
            name="decentrale_procedure_label",
            field=models.CharField(
                blank=True,
                help_text="Label die de context van de procedure beschrijft.",
                max_length=100,
                verbose_name="decentrale procedure label",
            ),
        ),
    ]
