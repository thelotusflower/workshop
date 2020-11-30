from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.db import transaction
from blog.forms import SignupForm, LoginForm
from blog.models import BlogPost, BlogSection


#def index_view(request):
#    return HttpResponse('<html><body> This is index </body></html>')

# def index_view(request):
#     # отдаем шаблон
#     # Django лоадеры шаблонов
#     # loader.get_template возвращает Template объект по заданному имени.
#     template = loader.get_template('index.html')
#     context = {
#         'user': request.user,
#         'site_name': 'Workshop Blog',
#     }
#     return HttpResponse(template.render(context, request=request))


# def index_view(request):
#     if request.method == 'GET':
#         return
#     elif request.method == 'POST':
#         return
#
#     context = {'user': request.user}
#     return render(request, 'index.html', context)


# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/#templateview
# class IndexView(generic.TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         context['sitename'] = 'DJANGO BLOG'
#         return context


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        section_slug = self.kwargs.get('section')
        if section_slug:
            section = BlogSection.objects.get(slug='auto')

            queryset = BlogSection.objects.all_sections_with_auto_at_start()

            blog_posts = section.related_posts.all()
        else:
            blog_posts = BlogPost.objects.all()
            
        
        context['blog_posts'] = blog_posts
        
        return context


# 1 Iteration
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/#view
class SignupView(generic.View):
    def get(self, request, *args, **kwargs):
        form = SignupForm()
        context = {'user': request.user, 'form': form}
        return render(request, 'signup.html', context)

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                )
            
            login(request, user)

            return HttpResponseRedirect(reverse('blog:main-page'))
        else:
            context = {'user': request.user, 'form': form}
            return render(request, 'signup.html', context)

        

# # 2 iteration
# class SignupView(generic.FormView):
#     form_class = ''


# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#createview
class PostCreateView(generic.CreateView):
    template_name = 'blogpost_form.html'
    model = BlogPost
    fields = ['name', 'author', 'slug', 'text', 'short_description', 'sections']

    def get_success_url(self):
        return reverse('blog:post', self.object.slug)


# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#detailview
class PostView(generic.DetailView):
    model = BlogPost
    template_name = 'blogpost.html'
    context_object_name = 'blog_post'


# 1 iteration
# class LoginView(generic.FormView):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         print(f'{username=} {password=}')
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             login(self.request, user)
#             return redirect('blog:main-page')
#
#         return self.form_invalid(form)
#
#     def form_invalid(self, form):
#         return self.render_to_response(
#             self.get_context_data
#             (
#                 form=form,
#                 is_login_or_password_invalid=True,
#             )
#         )

#2  Iteration 
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.views.LoginView
class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm


class LogoutView(auth_views.LogoutView):
    next_page = 'blog:main-page'
    
