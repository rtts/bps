from django import forms
from django.template import loader

class PandocEditor(forms.widgets.Textarea):
    """Form widget specifically for editing PandocFields

    """
    def render(self, name, value, attrs={}):
        if hasattr(value, 'raw'):
            value = value.raw
        # return super().render(name, value, attrs)
        context = self.get_context(name, value, attrs)
        template = loader.get_template('pandocfield/widget.html')
        return template.render(context)

    class Media:
        css = {
            'all': ('pandocfield/pandocfield.css',)
        }
