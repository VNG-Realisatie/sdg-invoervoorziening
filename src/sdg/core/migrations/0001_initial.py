# Generated by Django 2.2.24 on 2021-09-15 12:50

from django.db import migrations, models
import django.db.models.deletion
import sdg.core.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Informatiegebied",
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
                    "code",
                    models.CharField(
                        help_text="De code van het desbetreffende informatiegebied.",
                        max_length=32,
                        unique=True,
                        verbose_name="code",
                    ),
                ),
                (
                    "informatiegebied",
                    models.CharField(
                        help_text="Het bij de gegevens behorende informatiegebied.",
                        max_length=80,
                        verbose_name="informatiegebied",
                    ),
                ),
                (
                    "informatiegebied_uri",
                    models.URLField(
                        help_text="Informatiegebied URI van landelijk product",
                        verbose_name="informatiegebied uri",
                    ),
                ),
            ],
            options={
                "verbose_name": "informatiegebied",
                "verbose_name_plural": "informatiegebieden",
            },
        ),
        migrations.CreateModel(
            name="Overheidsorganisatie",
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
                    "owms_identifier",
                    models.URLField(
                        help_text="De metadatastandaard voor informatie van de nederlandse overheid op internet.",
                        unique=True,
                        verbose_name="OWMS identifier",
                    ),
                ),
                (
                    "owms_pref_label",
                    models.CharField(
                        help_text="De wettelijk erkende naam van de organisatie.",
                        max_length=80,
                        verbose_name="OWMS pref label",
                    ),
                ),
                (
                    "owms_end_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="De endDate, zoals gevonden in het OWMS-model.",
                        null=True,
                        verbose_name="end date",
                    ),
                ),
            ],
            options={
                "verbose_name": "overheidsorganisatie",
                "verbose_name_plural": "overheidsorganisaties",
            },
        ),
        migrations.CreateModel(
            name="ProductenCatalogus",
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
                    "domein",
                    models.CharField(
                        help_text="Een afkorting die wordt gebruikt om het domein aan te duiden.",
                        max_length=5,
                        validators=[sdg.core.models.validators.validate_uppercase],
                        verbose_name="domein",
                    ),
                ),
                (
                    "versie",
                    models.PositiveIntegerField(
                        default=1,
                        help_text="Het versienummer van het producten catalogus.",
                        verbose_name="versie",
                    ),
                ),
                (
                    "naam",
                    models.CharField(
                        help_text="De naam van de producten catalogus.",
                        max_length=40,
                        verbose_name="naam",
                    ),
                ),
                (
                    "toelichting",
                    models.TextField(
                        blank=True,
                        help_text="Toelichting bij het catalogus.",
                        verbose_name="toelichting",
                    ),
                ),
            ],
            options={
                "verbose_name": "producten catalogus",
                "verbose_name_plural": "productcatalogi",
            },
        ),
        migrations.CreateModel(
            name="Thema",
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
                    "thema",
                    models.CharField(
                        help_text="Het thema dat verband houdt met de gegevens.",
                        max_length=512,
                        verbose_name="thema",
                    ),
                ),
                (
                    "thema_uri",
                    models.URLField(
                        help_text="Thema URI van landelijk product",
                        verbose_name="thema uri",
                    ),
                ),
                (
                    "informatiegebied",
                    models.OneToOneField(
                        help_text="Het informatiegebied met betrekking tot dit thema.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="thema",
                        to="core.Informatiegebied",
                        verbose_name="informatiegebied",
                    ),
                ),
            ],
            options={
                "verbose_name": "thema",
                "verbose_name_plural": "thema's",
            },
        ),
        migrations.CreateModel(
            name="UniformeProductnaam",
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
                    "upn_uri",
                    models.URLField(
                        help_text="Uniforme Productnaam URI van landelijk product",
                        verbose_name="UPN URI",
                    ),
                ),
                (
                    "upn_label",
                    models.CharField(
                        help_text="Het bijbehorende label. Zie https://standaarden.overheid.nl/owms/oquery/UPL-actueel.plain voor de volledige UPL. ",
                        max_length=255,
                        verbose_name="UPN label",
                    ),
                ),
                ("rijk", models.BooleanField(default=False, verbose_name="rijk")),
                (
                    "provincie",
                    models.BooleanField(default=False, verbose_name="provincie"),
                ),
                (
                    "waterschap",
                    models.BooleanField(default=False, verbose_name="waterschap"),
                ),
                (
                    "gemeente",
                    models.BooleanField(default=False, verbose_name="gemeente"),
                ),
                ("burger", models.BooleanField(default=False, verbose_name="burger")),
                ("bedrijf", models.BooleanField(default=False, verbose_name="bedrijf")),
                (
                    "dienstenwet",
                    models.BooleanField(default=False, verbose_name="dienstenwet"),
                ),
                ("sdg", models.BooleanField(default=False, verbose_name="sdg")),
                (
                    "autonomie",
                    models.BooleanField(default=False, verbose_name="autonomie"),
                ),
                (
                    "medebewind",
                    models.BooleanField(default=False, verbose_name="medebewind"),
                ),
                (
                    "aanvraag",
                    models.BooleanField(default=False, verbose_name="aanvraag"),
                ),
                (
                    "subsidie",
                    models.BooleanField(default=False, verbose_name="subsidie"),
                ),
                ("melding", models.BooleanField(default=False, verbose_name="melding")),
                (
                    "verplichting",
                    models.BooleanField(default=False, verbose_name="verplichting"),
                ),
                (
                    "digi_d_macht",
                    models.BooleanField(default=False, verbose_name="digi_d_macht"),
                ),
                (
                    "grondslag",
                    models.CharField(
                        blank=True, max_length=80, null=True, verbose_name="grondslag"
                    ),
                ),
                (
                    "grondslaglabel",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="grondslaglabel",
                    ),
                ),
                (
                    "grondslaglink",
                    models.URLField(
                        blank=True, null=True, verbose_name="grondslaglink"
                    ),
                ),
                (
                    "thema",
                    models.ForeignKey(
                        blank=True,
                        help_text="Het informatiegebied met betrekking tot dit thema.",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="upn",
                        to="core.Thema",
                        verbose_name="thema",
                    ),
                ),
            ],
            options={
                "verbose_name": "uniforme productnaam",
                "verbose_name_plural": "uniforme productnamen",
            },
        ),
    ]
