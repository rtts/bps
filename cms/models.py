import swapper
from django.db import models
from django.urls import reverse
from django.forms import TextInput, Select
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField
from polymorphic.models import PolymorphicModel
from numberedmodel.models import NumberedModel as Numbered

class VarCharField(models.TextField):
    '''Variable width CharField'''
    def formfield(self, **kwargs):
        kwargs.update({'widget': TextInput})
        return super().formfield(**kwargs)

class BasePage(Numbered, models.Model):
    '''Abstract base model for pages'''
    number = models.PositiveIntegerField(_('number'), blank=True)
    title = VarCharField(_('title'))
    slug = models.SlugField(_('slug'), blank=True, unique=True)
    menu = models.BooleanField(_('visible in menu'), default=True)

    def __str__(self):
        if not self.pk:
            return str(_('New page'))
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('cms:page', args=[self.slug])
        return reverse('cms:page')

    class Meta:
        abstract = True
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        ordering = ['number']

class BaseSection(Numbered, PolymorphicModel):
    '''Abstract base model for sections'''
    TYPES = [] # Will be populated by @register_model()
    page = models.ForeignKey(swapper.get_model_name('cms', 'Page'), verbose_name=_('page'), related_name='sections', on_delete=models.PROTECT)
    type = VarCharField(_('type'), blank=True)
    number = models.PositiveIntegerField(_('number'), blank=True)

    title = VarCharField(_('title'), blank=True)
    content = models.TextField(_('content'), blank=True)
    image = models.ImageField(_('image'), blank=True)
    video = EmbedVideoField(_('video'), blank=True, help_text=_('Paste a YouTube, Vimeo, or SoundCloud link'))
    button_text = VarCharField(_('button text'), blank=True)
    button_link = VarCharField(_('button link'), blank=True)

    def number_with_respect_to(self):
        return self.page.sections.all()

    def __str__(self):
        if not self.pk:
            return str(_('New section'))
        elif not self.title:
            return str(_('Untitled'))
        else:
            return self.title

    class Meta:
        abstract = True
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        ordering = ['number']

class Page(BasePage):
    '''Swappable page model'''
    class Meta(BasePage.Meta):
        swappable = swapper.swappable_setting('cms', 'Page')

class Section(BaseSection):
    '''Swappable section model'''
    class Meta(BaseSection.Meta):
        swappable = swapper.swappable_setting('cms', 'Section')
