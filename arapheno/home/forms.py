from django import forms

from autocomplete_light import shortcuts as autocomplete_light

class GlobalSearchForm(forms.Form):
    global_search = autocomplete_light.GenericModelChoiceField("GlobalSearchAutocomplete")
