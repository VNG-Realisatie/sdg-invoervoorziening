from django.db import models
from django.utils.translation import ugettext_lazy as _


class Token(models.Model):
    """Custom authorization token model without binding to a specific user."""

    key = models.CharField(_("key"), max_length=40, primary_key=True)

    contact_person = models.CharField(
        _("contactpersoon"),
        max_length=100,
        help_text=_("Naam van de contactpersoon"),
    )
    email = models.EmailField(
        _("email"),
        help_text=_("Email van de contactpersoon"),
    )

    organization = models.CharField(
        _("organisatie"),
        max_length=100,
        help_text=_("Naam van de organisatie"),
        blank=True,
    )
    application = models.CharField(
        _("applicatie"),
        max_length=100,
        help_text=_("Naam van de applicatie"),
        blank=True,
    )
    administration = models.CharField(
        _("administratie"),
        max_length=100,
        help_text=_("Naam van de administratie"),
        blank=True,
    )

    created = models.DateTimeField(
        _("aangemaakt"),
        auto_now_add=True,
        help_text=_("Wanneer het token is aangemaakt"),
    )
    modified = models.DateTimeField(
        _("aangepast"),
        auto_now=True,
        help_text=_("Wanneer het token is aangepast"),
    )

    class Meta:
        verbose_name = _("token")
        verbose_name_plural = _("tokens")

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        """Generate a random key."""
        from django.utils.crypto import get_random_string

        return get_random_string(
            length=40, allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789"
        )
