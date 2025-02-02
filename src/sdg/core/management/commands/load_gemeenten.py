from sdg.core.management.parsers import ParserCommand
from sdg.core.management.utils import load_gemeenten


class Command(ParserCommand):
    plural_object_name = "gemeenten"
    xml_column_names = [
        "prefLabel",
        "resourceIdentifier",
        "endDate",
    ]

    def handle(self, **options):
        super().handle(load_gemeenten, **options)
