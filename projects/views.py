from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Project, ProjectComments
from .forms import CommentForm


class All(TemplateView):
    template_name = 'projects/all.html'

    def get_context_data(self, **kwargs):
        context = super(All, self).get_context_data(** kwargs)
        context['page_title'] = 'Projects'
        context['projects'] = Project.objects.order_by('-timestamp')[:10]
        return context


class SingleProject(TemplateView):
    template_name = 'projects/single_project.html'

    def post(self, *args, **kwargs):
        context = self.get_context_data()
        context['comment_form'] = CommentForm(self.request.POST)
        if context['comment_form'].is_valid():
            new_comment = context['comment_form'].save(commit=False)
            new_comment.project = context['project']
            if self.request.user.is_authenticated():
                new_comment.author = self.request.user
            new_comment.save()
            return HttpResponseRedirect('#')
        else:
            return HttpResponseRedirect('#')

    def get_context_data(self, **kwargs):
        context = super(SingleProject, self).get_context_data(**kwargs)
        context['page_title'] = 'Projects'
        context['project'] = Project.objects.get(slug=self.kwargs['slug'])
        context['comments'] = ProjectComments.objects.filter(project=context['project']).order_by('-timestamp')
        context['comment_form'] = CommentForm()
        return context
