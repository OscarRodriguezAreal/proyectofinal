from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

from django.views.generic import DetailView

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'author', 'image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'author', 'image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    # Obtener el perfil del usuario
    user_profile = request.user.profile
    return render(request, 'profile/profile.html', {'profile': user_profile})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

@login_required
def edit_profile(request):
   
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirigir al perfil una vez que se guarden los cambios
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from blog.models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Verificar si el perfil del usuario ya existe
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)  # Crear un perfil solo si no existe

            return redirect('profile')  # Redirigir al perfil del usuario
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render

def add_author(request):
    return render(request, 'blog/add_author.html')
def add_category(request):
    return render(request, 'blog/add_category.html')
def add_post(request):
    return render(request, 'blog/add_post.html')
def search_post(request):
    return render(request, 'blog/search_post.html')
from django.shortcuts import render
from .models import Blog  

def home(request):
    blogs = Blog.objects.all()  
    return render(request, 'home.html', {'blogs': blogs})

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # o el nombre correcto de tu url de login
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserEditForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile  # Asumimos que el perfil ya existe

    if request.method == 'POST':
        # Obtener valores del formulario
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        if password:
            user.set_password(password)  # Cambiar contraseña
        user.save()

        profile.biografia = request.POST.get('biografia', '')
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()

        return redirect('login')  # Redirigimos para ver los cambios

    context = {
        'form': user,
        'perfil_form': profile,
    }
    return render(request, 'profile/edit_profile.html', context)

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'profile/profile.html', {'profile': profile})

from django.shortcuts import render
from .models import Blog  

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

from django.shortcuts import render, get_object_or_404, redirect


@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == "POST":
        blog.delete()
        return redirect('home')  # Cambiá si tu URL del inicio tiene otro nombre
    
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})