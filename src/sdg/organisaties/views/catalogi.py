from django.utils.translation import gettext as _

from rijkshuisstijl.views.generic import ListView as RHListView

from sdg.accounts.mixins import OverheidMixin
from sdg.core.models import ProductenCatalogus
from sdg.organisaties.models import LokaleOverheid
from sdg.producten.models import Product


class CatalogListView(OverheidMixin, RHListView):
    fields = [
        {"label": _("Naam"), "key": "_name"},
        {
            "label": _("Informatiegebied"),
            "key": "referentie_product__generiek_product__upn__thema__informatiegebied",
        },
        {"label": _("Aanwezig"), "key": "product_aanwezig"},
        {"label": _("Publicatie datum"), "key": "active_version__publicatie_datum"},
    ]
    order = "_name"

    model = Product
    required_roles = ["is_beheerder", "is_redacteur"]
    template_name = "organisaties/catalogi/list.html"
    paginate_by = 100

    def get_datagrid_config(self):
        config = {
            **super().get_datagrid_config(),
            "dom_filter": True,
        }
        return config

    def get_lokale_overheid(self):
        """
        Returns the LokaleOverheid object for local municipality.
        """
        self.lokale_overheid = LokaleOverheid.objects.get(pk=self.kwargs["pk"])
        return self.lokale_overheid

    def get_queryset(self):
        """
        Returns ProductenCatalogus objects for local municipality.
        """
        catalogs = ProductenCatalogus.objects.filter(
            lokale_overheid=self.lokale_overheid
        )

        return (
            super()
            .get_queryset()
            .filter(catalogus__in=catalogs)
            .active()
            .annotate_name()
            .select_related("catalogus__lokale_overheid")
            .select_related(
                "referentie_product__generiek_product__upn__thema__informatiegebied"
            )
        )
