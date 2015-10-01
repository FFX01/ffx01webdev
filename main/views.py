from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from projects.models import Project
from blog.models import BlogPost
from .forms import ContactForm


class Home(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['page_title'] = 'Home'
        context['projects'] = Project.objects.order_by('-timestamp')[:4]
        context['posts'] = BlogPost.objects.order_by('-timestamp')[:4]
        return context


class About(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['page_title'] = 'About'
        return context


class Links(TemplateView):
    template_name = 'main/links.html'

    def get_context_data(self, **kwargs):
        context = super(Links, self).get_context_data(**kwargs)
        context['page_title'] = 'Useful Links'
        return context


class Info(TemplateView):
    template_name = 'main/info.html'

    def get_context_data(self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        context['page_title'] = 'Information'
        return context


class Contact(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = 'main:thank_you'

    def form_valid(self, form):
        form.send_email()
        return super(Contact, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['page_title'] = 'Contact'
        return context


class ThankYou(TemplateView):
    template_name = 'main/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super(ThankYou, self).get_context_data(**kwargs)
        context['page_title'] = 'Thank You'
        return context

