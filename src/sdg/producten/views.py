from django.views.generic import DetailView, TemplateView

from sdg.accounts.mixins import OverheidRoleRequiredMixin
from sdg.producten.models import ProductSpecifiekInformatie


class ProductListView(OverheidRoleRequiredMixin, TemplateView):
    template_name = "producten/products.html"

    @staticmethod
    def get_required_roles():
        return ["is_beheerder", "is_redacteur"]


class ProductDetailView(OverheidRoleRequiredMixin, DetailView):
    template_name = "organisaties/overheid_detail.html"
    model = ProductSpecifiekInformatie


# TODO [US-02] (Lokatie)
class ContactEditView(OverheidRoleRequiredMixin, TemplateView):
    template_name = "organisaties/overheid_update.html"
