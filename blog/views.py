from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import BlogPost, PostComment
from .forms import CommentForm


class All(TemplateView):
    template_name = 'blog/all.html'

    def get_context_data(self, **kwargs):
        context = super(All, self).get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        context['posts'] = BlogPost.objects.order_by('-timestamp')[:10]
        return context


class SinglePost(TemplateView):
    template_name = 'blog/single_post.html'

    def post(self, *args, **kwargs):
        context = self.get_context_data()
        context['comment_form'] = CommentForm(self.request.POST)
        if context['comment_form'].is_valid():
            new_comment = context['comment_form'].save(commit=False)
            new_comment.post = context['blog']
            if self.request.user.is_authenticated():
                new_comment.author = self.request.user
            new_comment.save()
            return HttpResponseRedirect('#')
        else:
            return HttpResponseRedirect('#')

    def get_context_data(self, **kwargs):
        context = super(SinglePost, self).get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        context['blog'] = BlogPost.objects.get(slug=self.kwargs['slug'])
        context['comments'] = PostComment.objects.filter(post=context['blog']).order_by('-timestamp')
        context['comment_form'] = CommentForm()
        return context
