# Generated by Django 2.2.24 on 2021-09-21 12:59

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import sdg.core.db.fields
import sdg.producten.models.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organisaties", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeneriekProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "verplicht_product",
                    models.BooleanField(
                        help_text="Geeft aan of decentrale overheden verplicht zijn informatie over dit product te leveren.",
                        verbose_name="verplicht product",
                    ),
                ),
                (
                    "upn",
                    models.ForeignKey(
                        help_text="De uniforme productnaam met betrekking tot dit product.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="generiek_product",
                        to="core.UniformeProductnaam",
                    ),
                ),
                (
                    "verantwoordelijke_organisatie",
                    models.ForeignKey(
                        help_text="Organisatie verantwoordelijk voor de landelijke informatie",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="generiek_informatie",
                        to="core.Overheidsorganisatie",
                        verbose_name="verantwoordelijke organisatie",
                    ),
                ),
            ],
            options={
                "verbose_name": "generiek product",
                "verbose_name_plural": "generieke producten",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "doelgroep",
                    sdg.core.db.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("burgers", "Burgers"),
                                ("bedrijven", "Bedrijven"),
                            ],
                            max_length=32,
                        ),
                        default=list,
                        help_text="Geeft aan voor welke doelgroep het product is bedoeld: burgers, bedrijven of burgers en bedrijven. Wordt gebruikt wanneer een portaal informatie over het product ophaalt uit de invoervoorziening. Zo krijgen de ondernemersportalen de ondernemersvariant en de burgerportalen de burgervariant. ",
                        size=None,
                    ),
                ),
                (
                    "beschikbaar",
                    models.BooleanField(
                        default=False,
                        help_text="Geeft aan of het product al dan niet beschikbaar is.",
                        verbose_name="beschikbaar",
                    ),
                ),
                (
                    "versie",
                    models.PositiveIntegerField(
                        default=1,
                        help_text="Het versienummer van het item.",
                        verbose_name="versie",
                    ),
                ),
                (
                    "publicatie_datum",
                    models.DateTimeField(
                        help_text="De datum van publicatie van de product.",
                        verbose_name="publicatie datum",
                    ),
                ),
                (
                    "catalogus",
                    models.ForeignKey(
                        help_text="De catalogus waartoe dit product behoort.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="producten",
                        to="core.ProductenCatalogus",
                        verbose_name="catalogus",
                    ),
                ),
                (
                    "generiek_product",
                    models.ForeignKey(
                        blank=True,
                        help_text="Het generiek product voor het referentieproduct.",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="producten",
                        to="producten.GeneriekProduct",
                        verbose_name="generiek product",
                    ),
                ),
                (
                    "gerelateerde_producten",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Een verwijzing naar een gerelateerd product.",
                        related_name="_product_gerelateerde_producten_+",
                        to="producten.Product",
                        verbose_name="gerelateerd aan",
                    ),
                ),
                (
                    "lokaties",
                    models.ManyToManyField(
                        blank=True,
                        help_text="De locaties die zijn toegewezen aan de product.",
                        related_name="producten",
                        to="organisaties.Lokatie",
                        verbose_name="lokaties",
                    ),
                ),
                (
                    "referentie_product",
                    models.ForeignKey(
                        blank=True,
                        help_text="Een referentie naar een product. Het toewijzen van een referentieproduct veronderstelt automatisch dat dit product specifiek is.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="producten",
                        to="producten.Product",
                        verbose_name="referentie product",
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "producten",
            },
        ),
        migrations.CreateModel(
            name="Productuitvoering",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Het referentieproduct voor het product.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="uitvoeringen",
                        to="producten.Product",
                        verbose_name="referentie",
                    ),
                ),
            ],
            options={
                "verbose_name": "productuitvoering",
                "verbose_name_plural": "productuitvoeringen",
            },
        ),
        migrations.CreateModel(
            name="LocalizedProductuitvoering",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "taal",
                    models.CharField(
                        choices=[("nl", "Nederlands"), ("en", "Engels")],
                        help_text="De taal waarin de betreffende tekst is geschreven.ISO 639-1 (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)",
                        max_length=2,
                        verbose_name="taal",
                    ),
                ),
                (
                    "product_titel_uitvoering",
                    models.CharField(
                        help_text="De titel van de uitvoering van het product.",
                        max_length=50,
                        verbose_name="product titel uitvoering",
                    ),
                ),
                (
                    "productuitvoering",
                    models.ForeignKey(
                        help_text="De productuitvoering van deze vertaling.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="vertalingen",
                        to="producten.Productuitvoering",
                        verbose_name="productuitvoering",
                    ),
                ),
            ],
            options={
                "verbose_name": "vertaalde productuitvoering",
                "verbose_name_plural": "vertaalde productuitvoeringen",
            },
        ),
        migrations.CreateModel(
            name="LocalizedProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "taal",
                    models.CharField(
                        choices=[("nl", "Nederlands"), ("en", "Engels")],
                        help_text="De taal waarin de betreffende tekst is geschreven.ISO 639-1 (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)",
                        max_length=2,
                        verbose_name="taal",
                    ),
                ),
                (
                    "product_titel_decentraal",
                    models.CharField(
                        blank=True,
                        help_text="De titel van het decentrale product, die immers kan afwijken van de landelijke titel.",
                        max_length=50,
                        verbose_name="product titel decentraal",
                    ),
                ),
                (
                    "specifieke_tekst",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Decentrale omschrijving.",
                        verbose_name="specifieke tekst",
                    ),
                ),
                (
                    "verwijzing_links",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.URLField(
                            max_length=1000, verbose_name="url van verwijzing"
                        ),
                        blank=True,
                        default=list,
                        help_text="Decentrale verwijzingen.",
                        size=None,
                    ),
                ),
                (
                    "specifieke_link",
                    models.URLField(
                        blank=True,
                        help_text="URL decentrale productpagina.",
                        verbose_name="specifieke link",
                    ),
                ),
                (
                    "decentrale_link",
                    models.URLField(
                        blank=True,
                        help_text="Link naar decentrale productpagina voor burgers en / of bedrijven.",
                        verbose_name="decentrale link",
                    ),
                ),
                (
                    "datum_wijziging",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Decentrale overheden geven een wijzigingsdatum mee voor hun informatie. Deze datum wordt op het portaal getoond. ",
                        verbose_name="datum wijziging",
                    ),
                ),
                (
                    "procedure_beschrijving",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Procedurebeschrijving.",
                        verbose_name="procedure beschrijving",
                    ),
                ),
                (
                    "vereisten",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Vereisten auth/id/sign.",
                        verbose_name="vereisten",
                    ),
                ),
                (
                    "bewijs",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Bewijs (type/format).",
                        verbose_name="bewijs",
                    ),
                ),
                (
                    "bezwaar_en_beroep",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Bezwaar en beroep.",
                        verbose_name="bezwaar en beroep",
                    ),
                ),
                (
                    "kosten_en_betaalmethoden",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Kosten en betaalmethoden.",
                        verbose_name="kosten en betaalmethoden",
                    ),
                ),
                (
                    "uiterste_termijn",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Deadlines.",
                        verbose_name="uiterste termijn",
                    ),
                ),
                (
                    "wtd_bij_geen_reactie",
                    markdownx.models.MarkdownxField(
                        blank=True,
                        help_text="Wat te doen bij geen reactie.",
                        verbose_name="wtd bij geen reactie",
                    ),
                ),
                (
                    "decentrale_procedure_link",
                    models.URLField(
                        blank=True,
                        help_text="Link naar de procedure voor burgers en / of bedrijven.",
                        verbose_name="decentrale procedure link",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Het specifieke product van deze vertaling.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="vertalingen",
                        to="producten.Product",
                        verbose_name="specifieke product",
                    ),
                ),
            ],
            options={
                "verbose_name": "vertaald product",
                "verbose_name_plural": "vertaalde producten",
            },
            bases=(sdg.producten.models.mixins.ProductFieldMixin, models.Model),
        ),
        migrations.CreateModel(
            name="LocalizedGeneriekProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "taal",
                    models.CharField(
                        choices=[("nl", "Nederlands"), ("en", "Engels")],
                        help_text="De taal waarin de betreffende tekst is geschreven.ISO 639-1 (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)",
                        max_length=2,
                        verbose_name="taal",
                    ),
                ),
                (
                    "product_titel",
                    models.CharField(
                        help_text="De titel van het decentrale product, die immers kan afwijken van de landelijke titel.",
                        max_length=50,
                        verbose_name="product titel",
                    ),
                ),
                (
                    "generieke_tekst",
                    markdownx.models.MarkdownxField(
                        help_text="De Nationale Portalen schrijven een inleidende, algemene tekst over het product. Het idee is dat deze ",
                        verbose_name="generieke tekst",
                    ),
                ),
                (
                    "korte_omschrijving",
                    models.CharField(
                        help_text='Korte omschrijving van wat er op de pagina staat, gebruikt in de meta tags van de productpagina (meta name="description"). Deze tekst wordt gebruikt om te tonen wanneer de pagina wordt gevonden in een zoekmachine. ',
                        max_length=80,
                        verbose_name="korte omschrijving",
                    ),
                ),
                (
                    "datum_check",
                    models.DateTimeField(
                        help_text="De informatie over het product kan worden gewijzigd en gecontroleerd op actualiteit (gecheckt). De Nationale portalen houden bij wanneer de informatie voor het laasts is 'gecheckt'.  Deze datum wordt op het portaal getoond.",
                        verbose_name="datum check",
                    ),
                ),
                (
                    "verwijzing_links",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.URLField(
                            max_length=1000, verbose_name="url van verwijzing"
                        ),
                        blank=True,
                        default=list,
                        help_text="Zowel de Nationale Portalen als de decentrale overheden kunnen een x-tal 'verwijzingen' opnemen bij een product. Voorstel hierbij om zo'n 'verwijzing' te laten bestaan uit een -bij elkaar horende-  beschrijving en hyperlink. De tekst van artikel 9 geeft enkele voorbeelden hiervan: 'richtsnoeren/ NEN-specs bijv en ook links naar de wetgeving (dit laatste is inderdaad te verstaan als vertaling van 'Legal Acts'. Bart heeft dit bij Jurist van bNC (Vanessa) gecheckt. ",
                        size=None,
                    ),
                ),
                (
                    "landelijke_link",
                    models.URLField(
                        help_text="URL van de productpagina wanneer het een landelijk product betreft of de pagina met enkel generieke beschrijving van een decentraal product, bijvoorbeeld : https://ondernemersplein.kvk.nl/terrasvergunning. gebruikt voor o.a. notificeren, feedback & statistics en het kunnen bekijken van de generieke productinformatie (bv door gebruikers van de gemeentelijke invoervoorziening) ",
                        verbose_name="landelijke link",
                    ),
                ),
                (
                    "generiek_product",
                    models.ForeignKey(
                        help_text="Het generieke product van deze vertaling.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vertalingen",
                        to="producten.GeneriekProduct",
                        verbose_name="generiek product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vertaald generiek product",
                "verbose_name_plural": "Vertaalde generieke producten",
            },
            bases=(sdg.producten.models.mixins.ProductFieldMixin, models.Model),
        ),
    ]
