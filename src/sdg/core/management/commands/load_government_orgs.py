from sdg.core.management.parsers import ParserCommand
from sdg.core.management.utils import load_government_organisations


class Command(ParserCommand):
    plural_object_name = "government organisations"
    xml_column_names = [
        "prefLabel",
        "resourceIdentifier",
        "endDate",
    ]

    def handle(self, **options):
        super().handle(load_government_organisations, **options)
