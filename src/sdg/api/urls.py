from django.conf.urls import include
from django.urls import path

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularYAMLAPIView,
)
from vng_api_common import routers

from sdg.api.views import (
    CatalogusViewSet,
    LokaleOverheidViewSet,
    LokatieViewSet,
    ProductHistoryViewSet,
    ProductViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register("catalogi", CatalogusViewSet)
router.register(
    "producten",
    ProductViewSet,
    [
        routers.nested(
            "historie",
            ProductHistoryViewSet,
            basename="product-history",
        )
    ],
)
router.register("organisaties", LokaleOverheidViewSet)
router.register("locaties", LokatieViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path(
        "v1/",
        include(
            [
                path(
                    "openapi.yaml",
                    SpectacularYAMLAPIView.as_view(),
                    name="schema",
                ),
                path(
                    "openapi.json",
                    SpectacularJSONAPIView.as_view(),
                    name="schema",
                ),
                path(
                    "schema/",
                    SpectacularRedocView.as_view(url_name="schema"),
                    name="schema-redoc",
                ),
            ]
        ),
    ),
]
