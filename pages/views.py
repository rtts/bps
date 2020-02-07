from cms.forms import ContactForm
from cms.views import SectionView, SectionFormView
from cms.decorators import register_view

from autodidact.models import Course
from .models import *

@register_view(TextSection)
class TextView(SectionView):
    template_name = 'pages/sections/text.html'

@register_view(ButtonSection)
class ButtonView(SectionView):
    template_name = 'pages/sections/button.html'

@register_view(ImageSection)
class ImageView(SectionView):
    template_name = 'pages/sections/image.html'

@register_view(VideoSection)
class VideoView(SectionView):
    template_name = 'pages/sections/video.html'

@register_view(Breadcrumbs)
class BreadcrumbsView(SectionView):
    template_name = 'pages/sections/breadcrumbs.html'

@register_view(Courses)
class CoursesView(SectionView):
    template_name = 'pages/sections/courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.filter(active=True)
        context.update({
            'courses': courses,
        })
        return context
