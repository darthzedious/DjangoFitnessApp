class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholder()

    def add_placeholder(self):
        for field_name, field in self.fields.items():
            placeholder = field.widget.attrs.get('placeholder') or field.label or field_name.replace('_', ' ').capitalice()
            field.widget.attrs['placeholder'] = placeholder


class DisabledReadonlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_readonly()

    def disable_readonly(self):
        for field in self.fields.values(): # ('name': object_field)
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
