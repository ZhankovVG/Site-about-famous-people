from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, MenCreateForm, RegisterUserForm
from .models import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login



class PostView(ListView, View):
    def get(self, request):
        posts = Men.objects.all()
        cats = Category.objects.all()

        context = {
            'posts' : posts,
            'cats' : cats,
            'title' : 'Главная страница',
        }
        return render(request, 'men/main.html', context = context)

class MenPost(ListView, View):
    def get(self, request, post_slug):
        post = get_object_or_404(Men, slug = post_slug)
        cats = Category.objects.all()

        context = {
            'title' : 'Пост',
            'post' : post,
            'cats' : cats,
        }
        return render(request, 'men/show_post.html', context=context)

class MenCategory(ListView, View):
    def get(self, request, cat_id):
        posts = Men.objects.filter( cat_id = cat_id )
        cats = Category.objects.all()

        context = {
            'posts' : posts,
            'cats' : cats,
            'title' : 'О  постах',
        }

        return render(request, 'men/main.html', context = context)


def about(request):
    cats = Category.objects.all()

    context = {
        'title' : 'О нас',
        'cats' : cats,
    }
    return render(request, 'men/about.html', context)    


def create(request):
    cats = Category.objects.all()
    form = MenCreateForm
    error = ''

    if request.method == 'POST':
        form = MenCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно'

    data = {
        'cats' : cats,
        'title' : 'Добавить статью',
        'form' : form,
        'error' : error,
    }

    return render(request, 'men/create.html', data)

def feedback(request):
    return render(request, 'men/feedback.html')


def login(request):
    return render(request, 'men/login.html')


class MyprojectLoginView(LoginView):
    template_name = 'men/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User    
    template_name = 'men/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')
   
