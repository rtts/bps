from django.utils.translation import gettext_lazy as _
from cms.views import SectionView, SectionFormView
from cms.decorators import section_view
from cms.forms import ContactForm

from autodidact.models import Course

@section_view
class Text(SectionView):
    verbose_name = _('Text')
    fields = ['content']
    template_name = 'pages/sections/text.html'

@section_view
class Image(SectionView):
    verbose_name = _('Image')
    fields = ['image']
    template_name = 'pages/sections/image.html'

@section_view
class Video(SectionView):
    verbose_name = _('Video')
    fields = ['video']
    template_name = 'pages/sections/video.html'

@section_view
class Button(SectionView):
    verbose_name = _('Button')
    fields = ['href']
    template_name = 'pages/sections/button.html'

@section_view
class Breadcrumbs(SectionView):
    verbose_name = _('Breadcrumbs')
    fields = []
    template_name = 'pages/sections/breadcrumbs.html'

@section_view
class Courses(SectionView):
    verbose_name = _('Courses')
    fields = []
    template_name = 'pages/sections/courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.filter(active=True)
        context.update({
            'courses': courses,
        })
        return context
