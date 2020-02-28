from django.db import models
from django.conf import settings
from cms.models import BasePage, BaseSection
from cms.decorators import register_model

class Page(BasePage):
    '''Add custom fields here. Already existing fields: position, title,
    slug, menu

    '''

class Section(BaseSection):
    '''Add custom fields here. Already existing fields: type, position,
    title, content, image, video, href

    '''

@register_model('Text')
class TextSection(Section):
    fields = ['title', 'content']
    class Meta:
        proxy = True

@register_model('Button')
class ButtonSection(Section):
    fields = ['title', 'href']
    class Meta:
        proxy = True

@register_model('Image')
class ImageSection(Section):
    fields = ['title', 'image']
    class Meta:
        proxy = True

@register_model('Video')
class VideoSection(Section):
    fields = ['title', 'video']
    class Meta:
        proxy = True

@register_model('Breadcrumbs')
class Breadcrumbs(Section):
    fields = ['title']
    class Meta:
        proxy = True

@register_model('Courses')
class Courses(Section):
    fields = ['title']
    class Meta:
        proxy = True
