from django.forms.widgets import (
    CheckboxSelectMultiple as _CheckboxSelectMultiple,
    ChoiceWidget,
)


class ProductRadioSelect(ChoiceWidget):
    input_type = "radio"
    template_name = "forms/widgets/multiple_input.html"
    option_template_name = "forms/widgets/radio_option.html"


class CheckboxSelectMultiple(_CheckboxSelectMultiple):
    template_name = "forms/widgets/multiple_input.html"
    option_template_name = "forms/widgets/checkbox_option.html"
