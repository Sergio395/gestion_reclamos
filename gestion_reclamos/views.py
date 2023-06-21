from django.views.generic import TemplateView

class logout_page(TemplateView):
    template_name = 'registration/_logged_out.html'