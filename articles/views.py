
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Articles
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class HomePage (ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = "articles"
    ordering = ['-date_created']
    paginate_by = 2

class ReadM(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'articles/articles_detail.html'

# @login_required
class CreateArticle(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'articles/new_article.html'
    fields = ['title', 'pics', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)