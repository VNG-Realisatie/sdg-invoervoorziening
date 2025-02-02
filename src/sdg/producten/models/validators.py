from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, _lazy_re_compile
from django.utils.translation import ugettext_lazy as _

no_html_validator = RegexValidator(
    _lazy_re_compile(r"<(.*)>.*?|<(.*) \>"),
    message=_(
        "Het veld mag geen HTML-tags bevatten. Zorg ervoor dat de tabel een header rij heeft."
    ),
    code="invalid",
    inverse_match=True,
)


def validate_no_html(value):
    return no_html_validator(value)


def validate_product(product):
    """Validate a product (specific / reference).
    - If `product_aanwezig` is False, the product must declare `product_aanwezig_toelichting`.
    """
    if product.product_aanwezig is False and not product.product_aanwezig_toelichting:
        raise ValidationError(
            _(
                "Het veld 'product_aanwezig_toelichting' is verplicht als het veld 'product_aanwezig' is uitgeschakeld."
            )
        )


def validate_specific_product(product):
    """Validate a specific product.
    - The product must have a reference product.
    - The product's catalog cannot be a referentie catalogus
    - The product cannot have a generic product.
    """

    if product.catalogus.is_referentie_catalogus:
        raise ValidationError(
            _("Dit specifieke product moet in een specifieke catalogus staan.")
        )
    if product.generiek_product:
        raise ValidationError(
            _(
                'Het veld "generiek_product" kan alleen worden toegevoegd als dit product een referentieproduct is.'
            )
        )
    if not product.referentie_product.catalogus.is_referentie_catalogus:
        raise ValidationError(
            _(
                "Het referentieproduct van dit product moet in een referentiecatalogus staan."
            )
        )


def validate_reference_product(product):
    """Validate a reference product.
    - The product's catalog must be a referentie catalogus.
    - The product must have a generic product.
    """

    if not product.catalogus.is_referentie_catalogus:
        raise ValidationError(
            _("Dit referentieproduct moet in een referentiecatalogus staan.")
        )
    if not product.generiek_product:
        raise ValidationError(
            _("Een referentieproduct moet een generiek product hebben.")
        )
