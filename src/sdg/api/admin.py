from django.contrib import admin

from sdg.api.models import Token, TokenAuthorization


class TokenAuthorizationInline(admin.TabularInline):
    model = TokenAuthorization
    extra = 1
    autocomplete_fields = ("lokale_overheid",)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("key", "created", "last_seen")
    readonly_fields = ("key", "last_seen")
    ordering = ("-created",)
    inlines = (TokenAuthorizationInline,)
