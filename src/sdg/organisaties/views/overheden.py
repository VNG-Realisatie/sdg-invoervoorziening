from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import UpdateView

from sdg.accounts.mixins import OverheidMixin
from sdg.core.types import Event
from sdg.organisaties.forms import LocatieInlineFormSet, LokaleOverheidForm
from sdg.organisaties.models import LokaleOverheid


class LokaleOverheidUpdateView(OverheidMixin, UpdateView):
    template_name = "organisaties/update.html"
    form_class = LokaleOverheidForm
    model = LokaleOverheid
    required_roles = ["is_redacteur"]

    def get_lokale_overheid(self):
        self.object = self.get_object()
        return self.object

    def form_valid(self, form):
        response = super().form_valid(form)
        Event.create_and_log(self.request, self.object, Event.UPDATE)
        messages.success(
            self.request,
            _(
                "De organisatie instellingen van gemeente {organisatie} zijn succesvol gewijzigd."
            ).format(organisatie=self.object),
        )
        return response
